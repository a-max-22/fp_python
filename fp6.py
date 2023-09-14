from enum import Enum

class CellState(Enum):
    CellFree = 0
    CapToday = 1
    Captured = 2

def MakeList(numItems, prev):
    if numItems == 0:
        return prev
    return MakeList(numItems - 1, [CellState.CellFree] + prev)

def MakeField(cols, rows, prevField):
    if rows == 0:
        return prevField
    currRow = MakeList(cols, [])
    return MakeField( cols, rows - 1, [currRow] + prevField)

class Field:
    def __init__(self, rows, cols):
        self.field = None if cols <= 0 or rows <= 0 else MakeField(cols, rows, [])
        self.cols = cols
        self.rows = rows 
        
    def is_in_field(self, pos):
        x,y = pos
        f_is_in_field = (0 <= x < self.cols and 0 <= y < self.rows)
        return f_is_in_field

def MarkCell(field, position, new_cell_state):
    if field.is_in_field(position):
        x,y = position
        field.field[y][x] = new_cell_state
    return field

def MarkCells(field, positions, curr_ind, cell_state):
    if curr_ind == len(positions):
        return field
    field =  MarkCell(field, positions[curr_ind], cell_state)
    return MarkCells(field, positions, curr_ind + 1, cell_state)


def FirstDay(field, first_day_positions):
    return MarkCells(field, first_day_positions, 0, CellState.Captured)


def MarkNearbyPosition(field, current_pos, delta_x, delta_y, new_cell_state, filter_func):
    x, y = current_pos
    new_pos = x + delta_x, y + delta_y
    num_cells_marked = 0
    if not field.is_in_field(new_pos):
        return field, num_cells_marked
        
    if not filter_func(field, new_pos):
        return field, num_cells_marked
    
    num_cells_marked = 1
    return MarkCell(field, new_pos, new_cell_state), num_cells_marked

def MarkUpper(field, current_pos, new_cell_state, filter_func):
    return MarkNearbyPosition(field, current_pos, 0, -1, new_cell_state, filter_func)

def MarkLower(field, current_pos, new_cell_state, filter_func):
    return MarkNearbyPosition(field, current_pos, 0, 1, new_cell_state, filter_func)

def MarkLeft(field, current_pos, new_cell_state, filter_func):
    return MarkNearbyPosition(field, current_pos, -1, 0, new_cell_state, filter_func)

def MarkRight(field, current_pos, new_cell_state, filter_func):
    return MarkNearbyPosition(field, current_pos, 1, 0, new_cell_state, filter_func)

def IsCapturedToday(field, pos):
    if not field.is_in_field(pos):
       return False
    x,y = pos
    return field.field[y][x] == CellState.CapToday

def IsFree(field, pos):
    if not field.is_in_field(pos):
       return False
    x,y = pos
    return field.field[y][x] == CellState.CellFree

def IsCaptured(field, pos):
    if not field.is_in_field(pos):
       return False
    x,y = pos
    return field.field[y][x] == CellState.Captured


def CaptureNearbyPos(field, current_pos):
    newState = CellState.CapToday
    filterFunc = IsFree
    field, capUpper = MarkUpper(field, current_pos, newState, filterFunc)
    field, capLower = MarkLower(field, current_pos, newState, filterFunc)
    field, capLeft  = MarkLeft(field, current_pos, newState, filterFunc)
    field, capRight  = MarkRight(field, current_pos, newState, filterFunc)
    
    return field, capUpper+capLower+capLeft+capRight

def CaptureCells(field, pos):
    num_cells_captured_nearby = 0
    if not IsCaptured(field, pos): 
        return field, num_cells_captured_nearby
    field, num_cells_captured_nearby = CaptureNearbyPos(field, pos)
    return field, num_cells_captured_nearby 

def GetNextPosition(field, pos):
    x,y = pos 
    if x >= field.cols:
        return 0, y + 1
    return x + 1, y

def CaptureCurrentCell(field, pos, num_cells_captured_prev):
    x,y = pos
    if x == field.cols and y == field.rows:
        return num_cells_captured_prev
    field, num_cells_captured = CaptureCells(field, pos)
    next_pos = GetNextPosition(field, pos)
     
    return CaptureCurrentCell(field, next_pos, num_cells_captured_prev + num_cells_captured)

def CaptureToday(field):
    pos = 0,0
    num_cells_captured_prev = 0
    return field, CaptureCurrentCell(field, pos, num_cells_captured_prev)

def TraverseCurrentCell(field, pos, func):
    x,y = pos
    if x == field.cols and y == field.rows:
        return field
    if field.is_in_field(pos):
        field = func(field, pos)
    next_pos = GetNextPosition(field, pos)
    return TraverseCurrentCell(field, next_pos, func)

def TraverseField(field, func):
    pos = 0,0
    return TraverseCurrentCell(field, pos, func)


def FinalizeCell(field, pos):
    x,y = pos
    if field.field[y][x] == CellState.CapToday:
        field.field[y][x] = CellState.Captured
    return field
    
def FinalizeCapturedCells(field):
    return TraverseField(field, FinalizeCell)


def ModelTrainigDay(field, num_captured_prev, num_days_passed):
    cells_num = field.cols * field.rows
    if num_captured_prev >= cells_num:
        return num_days_passed
    
    field, num_cells_captured = CaptureToday(field)
    field = FinalizeCapturedCells(field)
    return ModelTrainigDay(field, num_cells_captured + num_captured_prev, num_days_passed + 1)


def ModelTraining(field, first_day_pos):
    field = FirstDay(field, first_day_pos)
    num_cells_captured_initially = len(first_day_pos)
    return ModelTrainigDay(field, num_cells_captured_initially, 1)
    

def run():
    startcols, startrows = 5,6
    field = Field(startrows, startcols)
    first_day_pos = [(4,3), (1,1)]
    num_days_passed = ModelTraining(field, first_day_pos)
    print(num_days_passed)
    
    
run()

