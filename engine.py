import cv2
import chess
import chess.engine

def detect_chessboard(image_path):
    # Implement chessboard detection using OpenCV or other computer vision techniques
    # Extract the chessboard state (positions of pieces) from the image
    # Return the chessboard state as a FEN string

def find_best_moves(chessboard_fen):
    # Create a chess.Board object from the FEN string
    board = chess.Board(chessboard_fen)

    # Use a chess engine like Stockfish to evaluate and rank legal moves
    engine = chess.engine.SimpleEngine.popen_uci("stockfish\stockfish-windows-x86-64-avx2.exe")

    # Generate and evaluate legal moves
    legal_moves = list(board.legal_moves)
    move_scores = []

    for move in legal_moves:
        # Use the chess engine to evaluate the move
        with engine.analysis(board, multipv=3) as analysis:
            info = analysis.info
            best_moves = [info["pv"][0].uci(), info["pv"][1].uci(), info["pv"][2].uci()]
            score = info["score"].relative.score()

            move_scores.append((move.uci(), score, best_moves))

    # Sort moves by their evaluation scores (higher is better)
    move_scores.sort(key=lambda x: x[1], reverse=True)

    # Select the top three moves
    top_three_moves = move_scores[:3]

    return top_three_moves

if __name__ == "__main__":
    image_path = "captured_screenshot.png"
    # call screengrab.py
    chessboard_fen = detect_chessboard(image_path)
    
    if chessboard_fen:
        best_moves = find_best_moves(chessboard_fen)
        for i, (move, score, best_lines) in enumerate(best_moves, start=1):
            print(f"Move {i}: {move}, Score: {score}")
            print(f"Best Lines: {', '.join(best_lines)}")
    else:
        print("Chessboard not detected in the image.")
