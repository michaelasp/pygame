from typing import Optional, Union, Tuple, List, overload, Sequence

class _VectorElementwiseProxy2:
    def __add__(
        self, other: Union[float, Vector2, _VectorElementwiseProxy2]
    ) -> Vector2: ...
    def __radd__(
        self, other: Union[float, Vector2, _VectorElementwiseProxy2]
    ) -> Vector2: ...
    def __sub__(
        self, other: Union[float, Vector2, _VectorElementwiseProxy2]
    ) -> Vector2: ...
    def __rsub__(
        self, other: Union[float, Vector2, _VectorElementwiseProxy2]
    ) -> Vector2: ...
    def __mul__(
        self, other: Union[float, Vector2, _VectorElementwiseProxy2]
    ) -> Vector2: ...
    def __rmul__(
        self, other: Union[float, Vector2, _VectorElementwiseProxy2]
    ) -> Vector2: ...
    def __truediv__(
        self, other: Union[float, Vector2, _VectorElementwiseProxy2]
    ) -> Vector2: ...
    def __rtruediv__(
        self, other: Union[float, Vector2, _VectorElementwiseProxy2]
    ) -> Vector2: ...
    def __floordiv__(
        self, other: Union[float, Vector2, _VectorElementwiseProxy2]
    ) -> Vector2: ...
    def __rfloordiv__(
        self, other: Union[float, Vector2, _VectorElementwiseProxy2]
    ) -> Vector2: ...
    def __mod__(
        self, other: Union[float, Vector2, _VectorElementwiseProxy2]
    ) -> Vector2: ...
    def __rmod__(
        self, other: Union[float, Vector2, _VectorElementwiseProxy2]
    ) -> Vector2: ...
    def __pow__(
        self, power: Union[float, Vector2, _VectorElementwiseProxy2]
    ) -> Vector2: ...
    def __rpow__(
        self, power: Union[float, Vector2, _VectorElementwiseProxy2]
    ) -> Vector2: ...
    def __copy__(
        self, power: Union[float, Vector2, _VectorElementwiseProxy2]
    ) -> Vector2: ...
    def __flip__(
        self, power: Union[float, Vector2, _VectorElementwiseProxy2]
    ) -> Vector2: ...

class _VectorElementwiseProxy3:
    def __add__(
        self, other: Union[float, Vector3, _VectorElementwiseProxy3]
    ) -> Vector3: ...
    def __radd__(
        self, other: Union[float, Vector3, _VectorElementwiseProxy3]
    ) -> Vector3: ...
    def __sub__(
        self, other: Union[float, Vector3, _VectorElementwiseProxy3]
    ) -> Vector3: ...
    def __rsub__(
        self, other: Union[float, Vector3, _VectorElementwiseProxy3]
    ) -> Vector3: ...
    def __mul__(
        self, other: Union[float, Vector3, _VectorElementwiseProxy3]
    ) -> Vector3: ...
    def __rmul__(
        self, other: Union[float, Vector3, _VectorElementwiseProxy3]
    ) -> Vector3: ...
    def __truediv__(
        self, other: Union[float, Vector3, _VectorElementwiseProxy3]
    ) -> Vector3: ...
    def __rtruediv__(
        self, other: Union[float, Vector3, _VectorElementwiseProxy3]
    ) -> Vector3: ...
    def __floordiv__(
        self, other: Union[float, Vector3, _VectorElementwiseProxy3]
    ) -> Vector3: ...
    def __rfloordiv__(
        self, other: Union[float, Vector3, _VectorElementwiseProxy3]
    ) -> Vector3: ...
    def __mod__(
        self, other: Union[float, Vector3, _VectorElementwiseProxy3]
    ) -> Vector3: ...
    def __rmod__(
        self, other: Union[float, Vector3, _VectorElementwiseProxy3]
    ) -> Vector3: ...
    def __pow__(
        self, power: Union[float, Vector3, _VectorElementwiseProxy3]
    ) -> Vector3: ...
    def __rpow__(
        self, power: Union[float, Vector3, _VectorElementwiseProxy3]
    ) -> Vector3: ...
    def __copy__(
        self, power: Union[float, Vector3, _VectorElementwiseProxy3]
    ) -> Vector3: ...
    def __flip__(
        self, power: Union[float, Vector3, _VectorElementwiseProxy3]
    ) -> Vector3: ...

class Vector2:
    x: float
    y: float
    xx: Vector2
    xy: Vector2
    yx: Vector2
    yy: Vector2
    __hash__: None  # type: ignore
    @overload
    def __init__(
        self,
        x: Union[float, Tuple[float, float], List[float], Vector2] = 0,
    ) -> None: ...
    @overload
    def __init__(
            self,
            x: float,
            y: float,
    ) -> None: ...
    def __setitem__(self, key: int, value: float) -> None: ...
    @overload
    def __getitem__(self, i: int) -> float: ...
    @overload
    def __getitem__(self, s: slice) -> List[float]: ...
    def __add__(self, other: Vector2) -> Vector2: ...
    def __sub__(self, other: Vector2) -> Vector2: ...
    @overload
    def __mul__(self, other: Vector2) -> float: ...
    @overload
    def __mul__(self, other: float) -> Vector2: ...
    def __rmul__(self, other: float) -> Vector2: ...
    def __truediv__(self, other: float) -> Vector2: ...
    def __floordiv__(self, other: float) -> Vector2: ...
    def dot(self, other: Vector2) -> float: ...
    def cross(self, other: Vector2) -> Vector2: ...
    def magnitude(self) -> float: ...
    def magnitude_squared(self) -> float: ...
    def length(self) -> float: ...
    def length_squared(self) -> float: ...
    def normalize(self) -> Vector2: ...
    def normalize_ip(self) -> None: ...
    def is_normalized(self) -> bool: ...
    def scale_to_length(self, value: float) -> None: ...
    def reflect(self, other: Vector2) -> Vector2: ...
    def reflect_ip(self, other: Vector2) -> None: ...
    def distance_to(self, other: Union[Vector2, Sequence[float]]) -> float: ...
    def distance_squared_to(self, other: Vector2) -> float: ...
    def lerp(self, other: Vector2, value: float) -> Vector2: ...
    def slerp(self, other: Vector2, value: float) -> Vector2: ...
    def elementwise(self) -> _VectorElementwiseProxy2: ...
    def rotate(self, angle: float) -> Vector2: ...
    def rotate_rad(self, angle: float) -> Vector2: ...
    def rotate_ip(self, angle: float) -> None: ...
    def rotate_ip_rad(self, angle: float) -> None: ...
    def angle_to(self, other: Vector2) -> float: ...
    def as_polar(self) -> Tuple[float, float]: ...
    def from_polar(
        self, polar_value: Union[List[float], Tuple[float, float]]
    ) -> None: ...
    def update(
        self,
        x: Union[float, Vector2, Tuple[float, float], List[float]] = 0,
        y: float = 0,
    ) -> None: ...
    # def copy() method here
    # def flip() method here

class Vector3:
    x: float
    y: float
    z: float
    xx: Vector2
    xy: Vector2
    xz: Vector2
    yx: Vector2
    yy: Vector2
    yz: Vector2
    zx: Vector2
    zy: Vector2
    zz: Vector2
    xxx: Vector3
    xxy: Vector3
    xxz: Vector3
    xyx: Vector3
    xyy: Vector3
    xyz: Vector3
    xzx: Vector3
    xzy: Vector3
    xzz: Vector3
    yxx: Vector3
    yxy: Vector3
    yxz: Vector3
    yyx: Vector3
    yyy: Vector3
    yyz: Vector3
    yzx: Vector3
    yzy: Vector3
    yzz: Vector3
    zxx: Vector3
    zxy: Vector3
    zxz: Vector3
    zyx: Vector3
    zyy: Vector3
    zyz: Vector3
    zzx: Vector3
    zzy: Vector3
    zzz: Vector3
    __hash__: None  # type: ignore
    @overload
    def __init__(
        self,
        xyz: Union[float, Tuple[float, float, float], List[float], Vector3] = 0,
    ) -> None: ...
    @overload
    def __init__(
            self,
            x: float,
            y: float,
            z: float,
    ) -> None: ...
    def __setitem__(self, key: int, value: float) -> None: ...
    @overload
    def __getitem__(self, i: int) -> float: ...
    @overload
    def __getitem__(self, s: slice) -> List[float]: ...
    def __add__(self, other: Vector3) -> Vector3: ...
    def __sub__(self, other: Vector3) -> Vector3: ...
    @overload
    def __mul__(self, other: Vector3) -> float: ...
    @overload
    def __mul__(self, other: float) -> Vector3: ...
    def __rmul__(self, other: float) -> Vector3: ...
    def __truediv__(self, other: float) -> Vector3: ...
    def __floordiv__(self, other: float) -> Vector3: ...
    def dot(self, other: Vector3) -> float: ...
    def cross(self, other: Vector3) -> Vector3: ...
    def magnitude(self) -> float: ...
    def magnitude_squared(self) -> float: ...
    def length(self) -> float: ...
    def length_squared(self) -> float: ...
    def normalize(self) -> Vector3: ...
    def normalize_ip(self) -> None: ...
    def is_normalized(self) -> bool: ...
    def scale_to_length(self, value: float) -> None: ...
    def reflect(self, other: Vector3) -> Vector3: ...
    def reflect_ip(self, other: Vector3) -> None: ...
    def distance_to(self, other: Vector3) -> float: ...
    def distance_squared_to(self, other: Vector3) -> float: ...
    def lerp(self, other: Vector3, value: float) -> Vector3: ...
    def slerp(self, other: Vector3, value: float) -> Vector3: ...
    def elementwise(self) -> _VectorElementwiseProxy3: ...
    def rotate(self, angle: float, axis: Vector3) -> Vector3: ...
    def rotate_rad(self, angle: float, axis: Vector3) -> Vector3: ...
    def rotate_ip(self, angle: float, axis: Vector3) -> None: ...
    def rotate_ip_rad(self, angle: float, axis: Vector3) -> None: ...
    def rotate_x(self, angle: float) -> Vector3: ...
    def rotate_x_rad(self, angle: float) -> Vector3: ...
    def rotate_x_ip(self, angle: float) -> None: ...
    def rotate_x_ip_rad(self, angle: float) -> None: ...
    def rotate_y(self, angle: float) -> Vector3: ...
    def rotate_y_rad(self, angle: float) -> Vector3: ...
    def rotate_y_ip(self, angle: float) -> None: ...
    def rotate_y_ip_rad(self, angle: float) -> None: ...
    def rotate_z(self, angle: float) -> Vector3: ...
    def rotate_z_rad(self, angle: float) -> Vector3: ...
    def rotate_z_ip(self, angle: float) -> None: ...
    def rotate_z_ip_rad(self, angle: float) -> None: ...
    def angle_to(self, other: Vector3) -> float: ...
    def as_spherical(self) -> Tuple[float, float, float]: ...
    def from_spherical(self, spherical: Tuple[float, float, float]) -> None: ...
    @overload
    def update(
        self,
        xyz: Union[float, Tuple[float, float, float], List[float], Vector3] = 0,
    ) -> None: ...
    @overload
    def update(self, x: int, y: int, z: int) -> None: ...
    # def copy() method here
    # def flip() method here