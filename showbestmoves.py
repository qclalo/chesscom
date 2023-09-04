import cv2
import chess
import chess.svg
import chess.engine
from PIL import Image

# Function to draw the best moves on the chessboard image
def draw_best_moves(chessboard_image_path, best_moves):
    # Load the chessboard image
    image = cv2.imread(chessboard_image_path)
    
    # Initialize a chess board
    board = chess.Board()
    
    # Iterate through the best moves and apply them to the chess board
    for move in best_moves:
        chess_move = chess.Move.from_uci(move)
        board.push(chess_move)
    
    # Generate a SVG representation of the board with the best moves
    svg_board = chess.svg.board(board=board)
    
    # Convert the SVG image to a PIL image
    svg_image = Image.open(io.BytesIO(svg_board.encode('utf-8')))
    
    # Convert the PIL image to OpenCV format
    svg_image_cv = cv2.cvtColor(np.array(svg_image), cv2.COLOR_RGB2BGR)
    
    # Combine the chessboard image and the SVG image with the best moves
    result_image = cv2.addWeighted(image, 1, svg_image_cv, 1, 0)
    
    # Display the result image
    cv2.imshow("Chessboard with Best Moves", result_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    chessboard_image_path = "path_to_chessboard_image.jpg"
    
    # Replace with your best moves (e.g., "a2a4", "e7e5", "g1f3")
    best_moves = ["a2a4", "e7e5", "g1f3"]
    
    draw_best_moves(chessboard_image_path, best_moves)
