def to_proto_size(m):
    """convert from H0 meters to prototype meters"""
    return m * 87


def from_proto_size(m):
    """convert from prototype meters to H0 meters"""
    return m / 87


def to_proto_speed(m, s=1):
    """convert from H0 m/s to prototype km/h"""
    return to_proto_size(m) / s * 3.6 # result in km/h


def from_proto_speed(km, h=1):
    """convert from prototype km/h to H0 m/s"""
    return from_proto_size(km) / h / 3.6 # result in m/s
