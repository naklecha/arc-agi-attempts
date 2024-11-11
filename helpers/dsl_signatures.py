from typing import List, Union, Tuple, Any, Container, Callable, FrozenSet, Iterable
Boolean = bool
Integer = int
IntegerIterable = Tuple[Integer, Integer]
Numerical = Union[Integer, IntegerIterable]
IntegerSet = FrozenSet[Integer]
Grid = Iterable[Iterable[Integer]]
Cell = Tuple[Integer, IntegerIterable]
Object = FrozenSet[Cell]
Objects = FrozenSet[Object]
Indices = FrozenSet[IntegerIterable]
IndicesSet = FrozenSet[Indices]
Patch = Union[Object, Indices]
Element = Union[Object, Grid]
Piece = Union[Grid, Patch]
IterableIterable = Iterable[Iterable]
ContainerContainer = Container[Container]
ZERO = 0
ONE = 1
TWO = 2
THREE = 3
FOUR = 4
FIVE = 5
SIX = 6
SEVEN = 7
EIGHT = 8
NINE = 9
TEN = 10
F = False
T = True
NEG_ONE = -1
ORIGIN = (0, 0)
UNITY = (1, 1)
DOWN = (1, 0)
RIGHT = (0, 1)
UP = (-1, 0)
LEFT = (0, -1)
NEG_TWO = -2
NEG_UNITY = (-1, -1)
UP_RIGHT = (-1, 1)
DOWN_LEFT = (1, -1)
ZERO_BY_TWO = (0, 2)
TWO_BY_ZERO = (2, 0)
TWO_BY_TWO = (2, 2)
THREE_BY_THREE = (3, 3)

def identity(x: Any) -> Any:
    """ identity function  """

def add(a: Numerical, b: Numerical) -> Numerical:
    """ addition  """

def subtract(a: Numerical, b: Numerical) -> Numerical:
    """ subtraction  """

def multiply(a: Numerical, b: Numerical) -> Numerical:
    """ multiplication  """

def divide(a: Numerical, b: Numerical) -> Numerical:
    """ floor division  """

def invert(n: Numerical) -> Numerical:
    """ inversion with respect to addition  """

def even(n: Integer) -> Boolean:
    """ evenness  """

def double(n: Numerical) -> Numerical:
    """ scaling by two  """

def halve(n: Numerical) -> Numerical:
    """ scaling by one half  """

def flip(b: Boolean) -> Boolean:
    """ logical not  """

def equality(a: Any, b: Any) -> Boolean:
    """ equality  """

def contained(value: Any, container: Container) -> Boolean:
    """ element of  """

def combine(a: Container, b: Container) -> Container:
    """ union  """

def intersection(a: FrozenSet, b: FrozenSet) -> FrozenSet:
    """ returns the intersection of two containers  """

def difference(a: Container, b: Container) -> Container:
    """ difference  """

def dedupe(iterable: Iterable) -> Iterable:
    """ remove duplicates  """

def order(container: Container, compfunc: Callable) -> Iterable:
    """ order container by custom key  """

def repeat(item: Any, num: Integer) -> Iterable:
    """ repetition of item within vector  """

def greater(a: Integer, b: Integer) -> Boolean:
    """ greater  """

def size(container: Container) -> Integer:
    """ cardinality  """

def merge(containers: ContainerContainer) -> Container:
    """ merging  """

def maximum(container: IntegerSet) -> Integer:
    """ maximum  """

def minimum(container: IntegerSet) -> Integer:
    """ minimum  """

def valmax(container: Container, compfunc: Callable) -> Integer:
    """ maximum by custom function  """

def valmin(container: Container, compfunc: Callable) -> Integer:
    """ minimum by custom function  """

def argmax(container: Container, compfunc: Callable) -> Any:
    """ largest item by custom order  """

def argmin(container: Container, compfunc: Callable) -> Any:
    """ smallest item by custom order  """

def mostcommon(container: Container) -> Any:
    """ most common item  """

def leastcommon(container: Container) -> Any:
    """ least common item  """

def initset(value: Any) -> FrozenSet:
    """ initialize container  """

def both(a: Boolean, b: Boolean) -> Boolean:
    """ logical and  """

def either(a: Boolean, b: Boolean) -> Boolean:
    """ logical or  """

def increment(x: Numerical) -> Numerical:
    """ incrementing  """

def decrement(x: Numerical) -> Numerical:
    """ decrementing  """

def crement(x: Numerical) -> Numerical:
    """ incrementing positive and decrementing negative  """

def sign(x: Numerical) -> Numerical:
    """ sign  """

def positive(x: Integer) -> Boolean:
    """ positive  """

def toivec(i: Integer) -> IntegerIterable:
    """ vector pointing vertically  """

def tojvec(j: Integer) -> IntegerIterable:
    """ vector pointing horizontally  """

def sfilter(container: Container, condition: Callable) -> Container:
    """ keep elements in container that satisfy condition  """

def mfilter(container: Container, function: Callable) -> FrozenSet:
    """ filter and merge  """

def extract(container: Container, condition: Callable) -> Any:
    """ first element of container that satisfies condition  """

def toIterable(container: FrozenSet) -> Iterable:
    """ conversion to Iterable  """

def first(container: Container) -> Any:
    """ first item of container  """

def last(container: Container) -> Any:
    """ last item of container  """

def insert(value: Any, container: FrozenSet) -> FrozenSet:
    """ insert item into container  """

def remove(value: Any, container: Container) -> Container:
    """ remove item from container  """

def other(container: Container, value: Any) -> Any:
    """ other value in the container  """

def interval(start: Integer, stop: Integer, step: Integer) -> Iterable:
    """ range  """

def asIterable(a: Integer, b: Integer) -> IntegerIterable:
    """ constructs a Iterable  """

def product(a: Container, b: Container) -> FrozenSet:
    """ cartesian product  """

def pair(a: Iterable, b: Iterable) -> IterableIterable:
    """ zipping of two Iterables  """

def branch(condition: Boolean, if_value: Any, else_value: Any) -> Any:
    """ if else branching  """

def compose(outer: Callable, inner: Callable) -> Callable:
    """ function composition  """

def chain(h: Callable, g: Callable, f: Callable) -> Callable:
    """ function composition with three functions  """

def matcher(function: Callable, target: Any) -> Callable:
    """ construction of equality function  """

def rbind(function: Callable, fixed: Any) -> Callable:
    """ fix the rightmost argument  """

def lbind(function: Callable, fixed: Any) -> Callable:
    """ fix the leftmost argument  """

def power(function: Callable, n: Integer) -> Callable:
    """ power of function  """

def fork(outer: Callable, a: Callable, b: Callable) -> Callable:
    """ creates a wrapper function  """

def apply(function: Callable, container: Container) -> Container:
    """ apply function to each item in container  """

def rapply(functions: Container, value: Any) -> Container:
    """ apply each function in container to value  """

def mapply(function: Callable, container: ContainerContainer) -> FrozenSet:
    """ apply and merge  """

def papply(function: Callable, a: Iterable, b: Iterable) -> Iterable:
    """ apply function on two vectors  """

def mpapply(function: Callable, a: Iterable, b: Iterable) -> Iterable:
    """ apply function on two vectors and merge  """

def prapply(function: Callable, a: Container, b: Container) -> FrozenSet:
    """ apply function on cartesian product  """

def mostcolor(element: Element) -> Integer:
    """ most common color  """

def leastcolor(element: Element) -> Integer:
    """ least common color  """

def height(piece: Piece) -> Integer:
    """ height of grid or patch  """

def width(piece: Piece) -> Integer:
    """ width of grid or patch  """

def shape(piece: Piece) -> IntegerIterable:
    """ height and width of grid or patch  """

def portrait(piece: Piece) -> Boolean:
    """ whether height is greater than width  """

def colorcount(element: Element, value: Integer) -> Integer:
    """ number of cells with color  """

def colorfilter(objs: Objects, value: Integer) -> Objects:
    """ filter objects by color  """

def sizefilter(container: Container, n: Integer) -> FrozenSet:
    """ filter items by size  """

def asindices(grid: Grid) -> Indices:
    """ indices of all grid cells  """

def ofcolor(grid: Grid, value: Integer) -> Indices:
    """ indices of all grid cells with value  """

def ulcorner(patch: Patch) -> IntegerIterable:
    """ index of upper left corner  """

def urcorner(patch: Patch) -> IntegerIterable:
    """ index of upper right corner  """

def llcorner(patch: Patch) -> IntegerIterable:
    """ index of lower left corner  """

def lrcorner(patch: Patch) -> IntegerIterable:
    """ index of lower right corner  """

def crop(grid: Grid, start: IntegerIterable, dims: IntegerIterable) -> Grid:
    """ subgrid specified by start and dimension  """

def toindices(patch: Patch) -> Indices:
    """ indices of object cells  """

def recolor(value: Integer, patch: Patch) -> Object:
    """ recolor patch  """

def shift(patch: Patch, directions: IntegerIterable) -> Patch:
    """ shift patch  """

def normalize(patch: Patch) -> Patch:
    """ moves upper left corner to origin  """

def dneighbors(loc: IntegerIterable) -> Indices:
    """ directly adjacent indices  """

def ineighbors(loc: IntegerIterable) -> Indices:
    """ diagonally adjacent indices  """

def neighbors(loc: IntegerIterable) -> Indices:
    """ adjacent indices  """

def objects(grid: Grid, univalued: Boolean, diagonal: Boolean, without_bg: Boolean) -> Objects:
    """ objects occurring on the grid  """

def partition(grid: Grid) -> Objects:
    """ each cell with the same value part of the same object  """

def fgpartition(grid: Grid) -> Objects:
    """ each cell with the same value part of the same object without background  """

def uppermost(patch: Patch) -> Integer:
    """ row index of uppermost occupied cell  """

def lowermost(patch: Patch) -> Integer:
    """ row index of lowermost occupied cell  """

def leftmost(patch: Patch) -> Integer:
    """ column index of leftmost occupied cell  """

def rightmost(patch: Patch) -> Integer:
    """ column index of rightmost occupied cell  """

def square(piece: Piece) -> Boolean:
    """ whether the piece forms a square  """

def vline(patch: Patch) -> Boolean:
    """ whether the piece forms a vertical line  """

def hline(patch: Patch) -> Boolean:
    """ whether the piece forms a horizontal line  """

def hmatching(a: Patch, b: Patch) -> Boolean:
    """ whether there exists a row for which both patches have cells  """

def vmatching(a: Patch, b: Patch) -> Boolean:
    """ whether there exists a column for which both patches have cells  """

def manhattan(a: Patch, b: Patch) -> Integer:
    """ closest manhattan distance between two patches  """

def adjacent(a: Patch, b: Patch) -> Boolean:
    """ whether two patches are adjacent  """

def bordering(patch: Patch, grid: Grid) -> Boolean:
    """ whether a patch is adjacent to a grid border  """

def centerofmass(patch: Patch) -> IntegerIterable:
    """ center of mass  """

def palette(element: Element) -> IntegerSet:
    """ colors occurring in object or grid  """

def numcolors(element: Element) -> IntegerSet:
    """ number of colors occurring in object or grid  """

def color(obj: Object) -> Integer:
    """ color of object  """

def toobject(patch: Patch, grid: Grid) -> Object:
    """ object from patch and grid  """

def asobject(grid: Grid) -> Object:
    """ conversion of grid to object  """

def rot90(grid: Grid) -> Grid:
    """ quarter clockwise rotation  """

def rot180(grid: Grid) -> Grid:
    """ half rotation  """

def rot270(grid: Grid) -> Grid:
    """ quarter anticlockwise rotation  """

def hmirror(piece: Piece) -> Piece:
    """ mirroring along horizontal  """

def vmirror(piece: Piece) -> Piece:
    """ mirroring along vertical  """

def dmirror(piece: Piece) -> Piece:
    """ mirroring along diagonal  """

def cmirror(piece: Piece) -> Piece:
    """ mirroring along counterdiagonal  """

def fill(grid: Grid, value: Integer, patch: Patch) -> Grid:
    """ fill value at indices  """

def paint(grid: Grid, obj: Object) -> Grid:
    """ paint object to grid  """

def underfill(grid: Grid, value: Integer, patch: Patch) -> Grid:
    """ fill value at indices that are background  """

def underpaint(grid: Grid, obj: Object) -> Grid:
    """ paint object to grid where there is background  """

def hupscale(grid: Grid, factor: Integer) -> Grid:
    """ upscale grid horizontally  """

def vupscale(grid: Grid, factor: Integer) -> Grid:
    """ upscale grid vertically  """

def upscale(element: Element, factor: Integer) -> Element:
    """ upscale object or grid  """

def downscale(grid: Grid, factor: Integer) -> Grid:
    """ downscale grid  """

def hconcat(a: Grid, b: Grid) -> Grid:
    """ concatenate two grids horizontally  """

def vconcat(a: Grid, b: Grid) -> Grid:
    """ concatenate two grids vertically  """

def subgrid(patch: Patch, grid: Grid) -> Grid:
    """ smallest subgrid containing object  """

def hsplit(grid: Grid, n: Integer) -> Iterable:
    """ split grid horizontally  """

def vsplit(grid: Grid, n: Integer) -> Iterable:
    """ split grid vertically  """

def cellwise(a: Grid, b: Grid, fallback: Integer) -> Grid:
    """ cellwise match of two grids  """

def replace(grid: Grid, replacee: Integer, replacer: Integer) -> Grid:
    """ color substitution  """

def switch(grid: Grid, a: Integer, b: Integer) -> Grid:
    """ color switching  """

def center(patch: Patch) -> IntegerIterable:
    """ center of the patch  """

def position(a: Patch, b: Patch) -> IntegerIterable:
    """ relative position between two patches  """

def index(grid: Grid, loc: IntegerIterable) -> Integer:
    """ color at location  """

def canvas(value: Integer, dimensions: IntegerIterable) -> Grid:
    """ grid construction  """

def corners(patch: Patch) -> Indices:
    """ indices of corners  """

def connect(a: IntegerIterable, b: IntegerIterable) -> Indices:
    """ line between two points  """

def cover(grid: Grid, patch: Patch) -> Grid:
    """ remove object from grid  """

def trim(grid: Grid) -> Grid:
    """ trim border of grid  """

def move(grid: Grid, obj: Object, offset: IntegerIterable) -> Grid:
    """ move object on grid  """

def tophalf(grid: Grid) -> Grid:
    """ upper half of grid  """

def bottomhalf(grid: Grid) -> Grid:
    """ lower half of grid  """

def lefthalf(grid: Grid) -> Grid:
    """ left half of grid  """

def righthalf(grid: Grid) -> Grid:
    """ right half of grid  """

def vfrontier(location: IntegerIterable) -> Indices:
    """ vertical frontier  """

def hfrontier(location: IntegerIterable) -> Indices:
    """ horizontal frontier  """

def backdrop(patch: Patch) -> Indices:
    """ indices in bounding box of patch  """

def delta(patch: Patch) -> Indices:
    """ indices in bounding box but not part of patch  """

def gravitate(source: Patch, destination: Patch) -> IntegerIterable:
    """ direction to move source until adjacent to destination  """

def inbox(patch: Patch) -> Indices:
    """ inbox for patch  """

def outbox(patch: Patch) -> Indices:
    """ outbox for patch  """

def box(patch: Patch) -> Indices:
    """ outline of patch  """

def shoot(start: IntegerIterable, direction: IntegerIterable) -> Indices:
    """ line from starting point and direction  """

def occurrences(grid: Grid, obj: Object) -> Indices:
    """ locations of occurrences of object in grid  """

def frontiers(grid: Grid) -> Objects:
    """ set of frontiers  """

def compress(grid: Grid) -> Grid:
    """ removes frontiers from grid  """

def hperiod(obj: Object) -> Integer:
    """ horizontal periodicity  """

def vperiod(obj: Object) -> Integer:
    """ vertical periodicity  """