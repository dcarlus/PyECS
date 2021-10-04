import random

import pygame
from ecs.components import Component, ComponentFactory
from ecs.entities import Entity
from ecs.systems import SystemProcessing, System
from game.appdata import SystemName
from engine.graphics.geometry import Point
from game.components.engine.positioncomponent import PositionComponent
from game.components.engine.spritecomponent import SpriteComponent
from game.components.gameplay.charastatscomponent import CharacterPropertiesComponent

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

    def pre(self, linkedSystems: {str, System}) -> [Entity]:
        """Prepare work before run."""
        aiComponentsList: [AIComponent] = self.m_components.allComponents()
        charPropsSystem: System = linkedSystems[SystemName.characterProperties()]
        botEntitiesList: [Entity] = []

        # List all the entities bearing an AI component and a Character Properties component.
        for component in aiComponentsList:
            entity: Entity = component.entityValue
            charPropsSystem: [System] = linkedSystems[SystemName.characterProperties()]

            if charPropsSystem.componentFor(entity) is not None:
                botEntitiesList.append(component.entityValue)

        # Entities with a CharacterPropertiesComponent, it should be good to fight against them!
        for ai in aiComponentsList:
            changeTarget: bool = False

            if ai.target is None:
                changeTarget = True
            else:
                targetProps: CharacterPropertiesComponent = charPropsSystem.componentFor(ai.target)

                if targetProps is None or targetProps.life == 0:
                    changeTarget = True

            if changeTarget:
                ai.target = random.choice(botEntitiesList)

        return []

    def run(self, linkedSystems: {str, System}) -> [Entity]:
        """Perform the AIComponents processing."""
        aiComponentsList: [AIComponent] = self.m_components.allComponents()
        positionSystem: System = linkedSystems[SystemName.position()]
        spriteSystem: System = linkedSystems[SystemName.sprite()]
        charPropsSystem: System = linkedSystems[SystemName.characterProperties()]

        for component in aiComponentsList:
            entity: Entity = component.entityValue
            position: PositionComponent = positionSystem.componentFor(entity)
            sprite: SpriteComponent = spriteSystem.componentFor(entity).sprite
            charProps: CharacterPropertiesComponent = charPropsSystem.componentFor(entity)

            targetEntity: Entity = component.target
            targetPosition: PositionComponent = positionSystem.componentFor(targetEntity)
            targetSprite: SpriteComponent = spriteSystem.componentFor(targetEntity).sprite
            targetCharProps: CharacterPropertiesComponent = charPropsSystem.componentFor(targetEntity)

            if not sprite.collides(targetSprite):
                # Move towards the target.
                position.x = position.x + (charProps.speed if position.x < targetPosition.x else -charProps.speed)
                position.y = position.y + (charProps.speed if position.y < targetPosition.y else -charProps.speed)
            else:
                # Attack the target.
                targetCharProps.life = max(0, targetCharProps.life - charProps.attack)

        return []


