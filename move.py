import config

class Move:

    def __init__(self):
        self.current_chance_is_black = config.black_plays_first #my chance = black

    def can_move(self,pieces):
        for y in range(8):
            for x in range(8):
                if self.check_current_move_validity(x,y,pieces):
                    return True
        return False

    def check_current_move_validity(self, x, y, pieces):
        if pieces.pieces[y][x] != 0:
            return False, []

        flips = []
        color = 1 if self.current_chance_is_black else 2

        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
            _x, _y = x,y 
            _x += dr
            _y += dc
            if 0<=_x and _x<8 and 0<=_y and _y<8:
                if pieces.pieces[_y][_x] == 3 - color:
                    temp_flips = []
                    while (0 <= _x < 8 and 0 <= _y < 8) and pieces.pieces[_y][_x] == 3 - color:
                        print('r and c are of opp color', (_x,_y))
                        temp_flips.append((_x,_y))
                        _x += dr
                        _y += dc
                    if 0 <= _x < 8 and 0 <= _y < 8 and pieces.pieces[_y][_x] == color and len(temp_flips) > 0:
                        flips.extend(temp_flips)
            else:
                continue

        return len(flips) > 0, flips

