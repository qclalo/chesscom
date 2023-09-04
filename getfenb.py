import cv2
import chess
import chess.engine
from board_to_fen.predict import get_fen_from_image_path
from screengrab import capture_screenshot
from showboard import display_image
import pyperclip

def detect_chessboard(image_path):
    # Implement chessboard detection using OpenCV or other computer vision techniques
    # Extract the chessboard state (positions of pieces) from the image
    # Return the chessboard state as a FEN string
    a = get_fen_from_image_path(image_path, black_view = True)
    return add_black_to_move_and_castling_rights(a)

def add_black_to_move_and_castling_rights(original_fen):
    # By default, assume it's White's turn to move
    # and that castling rights are available for both sides.
    modified_fen = original_fen + " b KQkq - 1 0"
    return modified_fen

if __name__ == "__main__":

    x1, y1 = 265, 140
    x2, y2 = 1070, 140
    x3, y3 = 265, 945
    x4, y4 = 1070, 945
    
    x1, y1 = 265, 140
    x2, y2 = 1070, 140
    x3, y3 = 265, 945
    x4, y4 = 1070, 945
    
    capture_screenshot(x1, y1, x2, y2, x3, y3, x4, y4)
    image_path = "captured_screenshot.png"
    chessboard_fen = detect_chessboard(image_path)
    pyperclip.copy(chessboard_fen)
    print(chessboard_fen)
