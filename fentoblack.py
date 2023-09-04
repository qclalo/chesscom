def change_side_to_move(fen):
    # Split the FEN string into its components
    parts = fen.split(' ')
    
    # Modify the side to move part from 'w' to 'b'
    parts[1] = 'b'
    
    # Recreate the modified FEN string
    modified_fen = ' '.join(parts)
    
    return modified_fen

# Example usage:
original_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
modified_fen = change_side_to_move(original_fen)
print(modified_fen)
