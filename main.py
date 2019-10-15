from vehicle import Vehicle
from vehicle_exception import VehicleException
from motorcycle import Motorcycle
    
    
def main():
    try:
        m = Motorcycle(60, 2, "red")
        print(m)
        
        m.drive(4)
        print(m)
        
        m.honk()
        
        v = Vehicle(120, 4, "blue")
        print(v)
        
        v.drive(-3)
        print(v)
        
        v.honk()
    except VehicleException as e:
        print(e)
    else:
        print("Program completed successfully.")
    
    
if __name__=="__main__":
    main()




