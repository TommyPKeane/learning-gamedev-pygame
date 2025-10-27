"""Checkers Game | Main Python Module for Game Runtime with pygame

TODO (tommypkeane): Overwrite example game logic with Checkers game.

References:
    - https://www.pygame.org/docs/
"""
import argparse
import datetime
import logging

import pygame


module_logger = logging.getLogger(__name__)

MILLISECONDS_PER_SECOND: int = 1_000


def runtime_loop(
    screen_obj: pygame.Surface,
    clock_obj: pygame.time.Clock,
    player_position_start: pygame.Vector2,
    max_tick_rate_per_sec: int = 60,
) -> None:
    """Run the Main Loop for the pygame Runtime

    Args:
        screen_obj (pygame.Surface): ...
        clock_obj (pygame.time.Clock): ...
        player_position_start (pygame.Vector2): ...
        max_tick_rate_per_sec (int, optional): ...

    Returns:
        None: Nothing is returned, the Game Loop runs and exits when the User quits the
            Game
    """
    delta_time_ms: float = 0
    game_is_running: bool = True

    player_position_obj = player_position_start

    screen_obj.fill("black")

    while game_is_running:

        for event_obj in pygame.event.get():
            if event_obj.type == pygame.QUIT:
                game_is_running = False
                continue
            else:
                pass

        # Example Drawing
        pygame.draw.circle(
            screen_obj,
            "red",
            player_position_obj,
            40,
        )

        keys: dict = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            player_position_obj.y -= 300 * delta_time_ms
        else:
            pass

        if keys[pygame.K_s]:
            player_position_obj.y += 300 * delta_time_ms
        else:
            pass

        if keys[pygame.K_a]:
            player_position_obj.x -= 300 * delta_time_ms
        else:
            pass

        if keys[pygame.K_d]:
            player_position_obj.x += 300 * delta_time_ms
        else:
            pass

        if keys[pygame.K_k]:
            screen_obj.fill("black")
        else:
            pass


        pygame.display.flip()

        delta_time_ms = clock_obj.tick(max_tick_rate_per_sec) / MILLISECONDS_PER_SECOND
    else:
        pass

    return None


if __name__ == "__main__":
    cli_parser_obj = argparse.ArgumentParser(
        description="Checkers (via pygame)",
    )

    cli_parser_obj.add_argument(
        "--max_tick_rate_per_sec",
        type=int,
        default=60,
        help=(
            "Maximum framerate setting in [fps]."
        ),
    )

    cli_parser_obj.add_argument(
        "-l",
        "--logging_level",
        type=logging.getLevelName,
        default=logging.INFO,
        help="Python Logging Level.",
    )

    cli_args = cli_parser_obj.parse_args()

    logging.basicConfig(
        level=cli_args.logging_level,
        handlers=[
            logging.StreamHandler(),  # stdout
        ],
    )

    clock_obj: pygame.time.Clock = pygame.time.Clock()
    max_tick_rate_per_sec: int = 60

    module_logger.info("🕹️ Starting Game...")

    pygame.init()

    screen_obj = pygame.display.set_mode(
        (1280, 720)
    )

    screen_center_vec: pygame.Vector2 = pygame.Vector2(
        screen_obj.get_width() / 2,
        screen_obj.get_height() / 2,
    )

    module_logger.info("🎲 Game begins...")

    runtime_loop(
        screen_obj=screen_obj,
        clock_obj=clock_obj,
        player_position_start=screen_center_vec,
        max_tick_rate_per_sec=max_tick_rate_per_sec,
    )

    module_logger.info("🏁 Done! Exiting Game 👋")
    pygame.quit()
