class Bus:
    def __init__(
        self,
        rating,
        load, 
        name,
        v_nom,
        x,
        y,
        v_mag_pu_set,
        v_mag_pu_min,
        v_mag_pu_max,
        control,
        Pd,
        Qd,
        Gs,
        Bs,
        area,
        v_ang_set,
        zone,
        bus_name         
                 ):
        self.rating = rating
        self.load = load
        self.name = name
        self.v_nom = v_nom
        self.x = x
        self.y = y
        self.v_mag_pu_set = v_mag_pu_set
        self.v_mag_pu_min = v_mag_pu_min
        self.v_mag_pu_max = v_mag_pu_max
        self.control = control
        self.Pd = Pd
        self.Qd = Qd
        self.Bs = Gs
        self.Bs = Bs
        self.area = area
        self.v_ang_set = v_ang_set
        self.zone = zone
        self.bus_name = bus_name
        self.connections = []

    def connect(self, bus):
        self.connections.insert(0, bus)