import argparse
import datetime
import logging

import pygame


module_logger: logging.Logger = logging.getLogger(__name__)


def create_gameboard(
    screen_obj: pygame.Surface,
    color_a: tuple[int, int, int, int],
    color_b: tuple[int, int, int, int],
    board_size: int = 8,
) -> None:
    """UI Drawing Logic for the Checkers Game Board

    Args:
        screen_obj (pygame.Surface): Surface instance for rendering and for determining
            the display size to proportionally size the Game Board
        color_a (tuple[int, int, int, int]): "Red" Checkers Board Tile Color
        color_b (tuple[int, int, int, int]): "Black" Checkers Board Tile Color
        board_size (int, optional): Total number of Tiles in Width and Height for the
            Checkeers Board

    Returns:
        None: Nothing is returned, Board is rendered on the Display Surface
    """
    screen_width: int = screen_obj.get_width()
    screen_height: int = screen_obj.get_height()

    square_size: int = screen_height // int(board_size * 1.25)

    left_top_begin: int = (
        screen_width // 2 - ((board_size // 2) * square_size),
        (screen_height - (square_size * board_size)) // 2,
    )

    for row_idx in range(board_size):
        for col_idx in range(board_size):
            tile_square_obj: pygame.Rect = pygame.Rect(
                left_top_begin[0] + (col_idx * square_size),
                left_top_begin[1] + (row_idx * square_size),
                square_size,
                square_size,
            )

            tile_color: tuple[int, int, int, int] = None

            if row_idx % 2 == 0:
                if col_idx % 2 == 0:
                    tile_color = color_b
                else:
                    tile_color = color_a
            else:
                if col_idx % 2 == 0:
                    tile_color = color_a
                else:
                    tile_color = color_b

            pygame.draw.rect(
                surface=screen_obj,
                color=tile_color,
                rect=tile_square_obj,
                width=0,  # Filled Rectangle
            )

    board_border_obj: pygame.Rect = pygame.Rect(
        left_top_begin[0],
        left_top_begin[1],
        (square_size * board_size),
        (square_size * board_size),
    )

    pygame.draw.rect(
        surface=screen_obj,
        color=(
            color_a[0],
            color_a[1],
            color_a[2],
            int(max(color_a[3] * 1.5, 255)),
        ),
        rect=board_border_obj,
        width=2,  # Filled Rectangle
    )

    return None
