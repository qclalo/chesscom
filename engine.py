import cv2
import chess
import chess.engine
from board_to_fen.predict import get_fen_from_image_path

def detect_chessboard(image_path):
    # Implement chessboard detection using OpenCV or other computer vision techniques
    # Extract the chessboard state (positions of pieces) from the image
    # Return the chessboard state as a FEN string
    return get_fen_from_image_path(image_path)

def find_best_moves(chessboard_fen):
    # Create a chess.Board object from the FEN string
    with chess.engine.SimpleEngine.popen_uci("stockfish\stockfish-windows-x86-64-avx2.exe") as engine:
        board = chess.Board(chessboard_fen)
        result = engine.play(board, chess.engine.Limit(depth=10))
        return result.move.uci()

if __name__ == "__main__":
    image_path = "captured_screenshot.png"
    # call screengrab.py
    chessboard_fen = detect_chessboard(image_path)
    
    if chessboard_fen:
        best_moves = find_best_moves(chessboard_fen)
        print("Best move:", best_moves)
    else:
        print("Chessboard not detected in the image.")
