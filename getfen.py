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
    a = get_fen_from_image_path(image_path)
    return add_white_to_move_and_castling_rights(a)

def add_white_to_move_and_castling_rights(original_fen):
    # By default, assume it's White's turn to move
    # and that castling rights are available for both sides.
    modified_fen = original_fen + " w KQkq - 0 1"
    return modified_fen


def find_best_moves(fen_position, num_moves=3, depth=20):
    with chess.engine.SimpleEngine.popen_uci("stockfish\stockfish-windows-x86-64-avx2.exe") as engine:
        board = chess.Board(fen_position)
        info = engine.analyse(board, chess.engine.Limit(depth=10), multipv=num_moves)
        
        top_moves = []
        for i, entry in enumerate(info):
            move = entry.get("pv")[0]  # Get the best move in the principal variation
            score = entry.get("score").relative.score()
            top_moves.append({"move": move.uci(), "score": score})
            
        return top_moves

if __name__ == "__main__":
    x1, y1 = 265, 140
    x2, y2 = 1070, 140
    x3, y3 = 265, 945
    x4, y4 = 1070, 945
    
    capture_screenshot(x1, y1, x2, y2, x3, y3, x4, y4)
    image_path = "captured_screenshot.png"
    chessboard_fen = detect_chessboard(image_path)
    pyperclip.copy(chessboard_fen)
    print(chessboard_fen)
