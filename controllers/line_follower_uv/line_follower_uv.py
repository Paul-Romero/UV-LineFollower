from controller import Robot, DistanceSensor, Motor
from time import sleep

# tiempo en [ms] de la simulación
TIME_STEP = 64
# velocidad maxima del robot
MAX_SPEED = 6.28

def run(robot):
    # inicializar LED
    led = robot.getDevice('led')
    # inicializar los sensores de distancia
    ps = []
    psNames = [
        'ds0', 'ds1', 'ds2', 'ds3',
        'ds4', 'ds5', 'ds6', 'ds7'
    ]
    # habilitar los sensores
    for i in range(8):
        ps.append(robot.getDevice(psNames[i]))
        ps[i].enable(TIME_STEP)
    
    # inicializar los motores
    leftMotor = robot.getDevice('left wheel motor')
    rightMotor = robot.getDevice('right wheel motor')
    leftMotor.setPosition(float('inf'))
    rightMotor.setPosition(float('inf'))
    leftMotor.setVelocity(0.0)
    rightMotor.setVelocity(0.0)
    
    # configuracion de sensores IR
    irRight = robot.getDevice('ir1')
    irRight.enable(TIME_STEP)
    irLeft = robot.getDevice('ir0')
    irLeft.enable(TIME_STEP)
    
    # bucle de ejecucion
    while robot.step(TIME_STEP) != -1:
        # encender LED UV
        led.set(1)
        # leer datos de los sensores
        irRightValue = irRight.getValue()
        irLeftValue = irLeft.getValue()
        psValues = []
        for i in range(8):
            psValues.append(ps[i].getValue())
        
        print("Read distance sensors: {}".format(psValues[0:6]))
        print("IR sensors: LEFT: {} RIGHT: {}".format(irLeftValue, irRightValue))
        
        # detercar obstaculos
        right_obstacle = psValues[1] > 80.0 or psValues[4] > 80.0 or psValues[2] > 80.0
        left_obstacle = psValues[0] > 80.0 or psValues[5] > 80.0
        
        # inicializar la velocidad del motor con un 50% de velocidad max
        leftSpeed = 0.5 * MAX_SPEED
        rightSpeed = 0.5 * MAX_SPEED
        
        # actuar de acuerdo a la pista
        if (irLeftValue < 1000) and (irRightValue >= 600) or right_obstacle:
            leftSpeed  = 0.5 * MAX_SPEED
            rightSpeed = -0.5 * MAX_SPEED
        elif (irLeftValue >= 600) and (irRightValue < 1000) or left_obstacle:
            leftSpeed  = -0.5 * MAX_SPEED
            rightSpeed = 0.5 * MAX_SPEED
        
        # mover el robot a la velocidad establecida
        leftMotor.setVelocity(leftSpeed)
        rightMotor.setVelocity(rightSpeed)


if __name__=='__main__':
    elBicho = Robot()
    sleep(1) # espera 1ms antes de comenzar; Crear un nuevo robot y copiar los elementos al nuevo robot. Luego probar las dos pistas nuevas
    run(elBicho)