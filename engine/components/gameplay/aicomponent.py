import random
from ecs.components import Component, ComponentFactory
from ecs.entities import Entity
from ecs.systems import SystemProcessing, System
from game.appdata import SystemName
from engine.geometry import Point
from ..spritecomponent import SpriteComponent
from .charastatscomponent import CharacterPropertiesComponent

class AIComponent(Component):
    """Component for making Characters act by themselves."""

    def __init__(self, entity: Entity):
        """Create a new AIComponent instance."""
        super().__init__(entity)
        self.m_target: Entity = None

    @property
    def target(self) -> Entity:
        """Get the target of the current intelligence."""
        return self.m_target

    @target.setter
    def target(self, other: Entity) -> None:
        """Set the new target of the current intelligence."""
        self.m_target = other


class AIProcessing(SystemProcessing):
    """System processing of AIComponents."""

    def __init__(self, components: ComponentFactory):
        """Create a new AIProcessing instance."""
        super().__init__(components)

    def selectTarget(self, linkedSystems: {str, System}, fromIndex: int, toIndex: int) -> None:
        """Give each character a target to attack."""
        aiComponentsList: [AIComponent] = self.m_components.allComponents()
        charPropsSystem: System = linkedSystems[SystemName.characterProperties()]
        botEntitiesList: [Entity] = []

        # List all the entities bearing an AI component and a Character Properties component.
        for index in range(fromIndex, toIndex):
            component: Component = aiComponentsList[index]
            entity: Entity = component.entityValue
            charPropsSystem: [System] = linkedSystems[SystemName.characterProperties()]

            if charPropsSystem.componentFor(entity) is not None:
                botEntitiesList.append(component.entityValue)

        # Entities with a CharacterPropertiesComponent, it should be good to fight against them!
        for index in range(fromIndex, toIndex):
            ai: Component = aiComponentsList[index]
            changeTarget: bool = False

            if ai.target is None:
                changeTarget = True
            else:
                targetProps: CharacterPropertiesComponent = charPropsSystem.componentFor(ai.target)

                if targetProps is None or targetProps.life == 0:
                    changeTarget = True

            if changeTarget:
                selectedEntity: Entity = random.choice(botEntitiesList)
                ai.target = selectedEntity if selectedEntity is not entity else None

    def processAI(self, linkedSystems: {str, System}, fromIndex: int, toIndex: int) -> None:
        """Process the AI itself."""
        aiComponentsList: [AIComponent] = self.m_components.allComponents()
        spriteSystem: System = linkedSystems[SystemName.sprite()]
        charPropsSystem: System = linkedSystems[SystemName.characterProperties()]

        for index in range(fromIndex, toIndex):
            component: Component = aiComponentsList[index]
            entity: Entity = component.entityValue
            sprite: SpriteComponent = spriteSystem.componentFor(entity).sprite
            charProps: CharacterPropertiesComponent = charPropsSystem.componentFor(entity)

            targetEntity: Entity = component.target

            if targetEntity is None:
                continue

            targetSprite: SpriteComponent = spriteSystem.componentFor(targetEntity).sprite
            targetCharProps: CharacterPropertiesComponent = charPropsSystem.componentFor(targetEntity)

            if not sprite.collides(targetSprite):
                # Move towards the target.
                shiftPosition: Point = Point()
                shiftPosition.x = charProps.speed if sprite.position.x < targetSprite.position.x else -charProps.speed
                shiftPosition.y = charProps.speed if sprite.position.y < targetSprite.position.y else -charProps.speed
                sprite.position = sprite.position + shiftPosition
                sprite.update()
            else:
                # Attack the target.
                targetCharProps.life = max(0, targetCharProps.life - charProps.attack)

    def run(self, linkedSystems: {str, 'System'}, fromIndex: int, toIndex: int) -> [Entity]:
        """Perform the Components processing. Returns a list of Entity to be removed by the World."""
        self.selectTarget(linkedSystems, fromIndex, toIndex)
        self.processAI(linkedSystems, fromIndex, toIndex)
        return []


