import cv2
import chess
import chess.engine
from board_to_fen.predict import get_fen_from_image_path
from screengrab import capture_screenshot
from showboard import display_image

def detect_chessboard(image_path):
    # Implement chessboard detection using OpenCV or other computer vision techniques
    # Extract the chessboard state (positions of pieces) from the image
    # Return the chessboard state as a FEN string
    return get_fen_from_image_path(image_path, black_view = True)

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
    # x1, y1 = 320, 175
    # x2, y2 = 1070, 175
    # x3, y3 = 320, 925
    # x4, y4 = 1070, 925

    x1, y1 = 265, 140
    x2, y2 = 1070, 140
    x3, y3 = 265, 945
    x4, y4 = 1070, 945
    
    capture_screenshot(x1, y1, x2, y2, x3, y3, x4, y4)
    image_path = "captured_screenshot.png"
    # call screengrab.py
    chessboard_fen = detect_chessboard(image_path)
    
    if chessboard_fen:
        best_moves = find_best_moves(chessboard_fen)
        print("Best move:", best_moves)
        display_image(image_path)
    else:
        print("Chessboard not detected in the image.")
