# from pymodbus.client import ModbusTcpClient
# from pymodbus.transaction import ModbusRtuFramer

import time
from pymodbus.client.sync import ModbusTcpClient as ModbusClient

UNIT = 0x1# numero de unidad
client = ModbusClient('192.168.0.248', port=502)
    
    # client = ModbusClient('localhost', port=5020, framer=ModbusRtuFramer)
    # client = ModbusClient(method='binary', port='/dev/ptyp0', timeout=1)
    # client = ModbusClient(method='ascii', port='/dev/ptyp0', timeout=1)
    # client = ModbusClient(method='rtu', port='/dev/ptyp0', timeout=1,baudrate=9600)
print(client.connect())

  
    # print("Mensaje en Binario: ",Mensaje)
        # rq = client.write_coil(0, True, unit=UNIT)#Escribe una sola salida (# Q0.0=1) a partir de Q0 indicado por el numero 1
        # rr = client.read_coils(0, 1, unit=UNIT)# Lee salidas segun se le indique
        # #rr.bits hace padding de ceros multiplos de 8
        # print("la salida de Q0.0 es", rr.bits )

        # #escritura y lectura de multiples salidas
        # rq = client.write_coils(1, [True]*8, unit=UNIT)
        # rr = client.read_coils(1, 8, unit=UNIT)
        # print("la salida de Q0.1-Q1.0 son", rr.bits )


        # # leer entradas discretas
        # rr=client.read_discrete_inputs(0,8, unit=UNIT)
        # print("la salida de I0.0-I0.7  es", rr.bits )

        # #escritura de un HR
    #rq = client.write_register(9000, 777783000, unit=UNIT) #Escribe en la posicion 1 Un 10
        # rr = client.read_holding_registers(1, 1, unit=UNIT)#Leemos los registros en la posicion 1
        # print("HR= ",rr.registers[0])#como sabemos que solo es un registro y esta en la posicion 0 lo leemos directamente pero podems leerlo dentro de un for


#/////////Conexion pruebas

print("·············")
# while True: #crear un ciclo de envio o recepcion de datos
                #escritura de un HR
#rq = client.write_registers(9000, [6, 77, 77, 83, 48, 48, 48]], unit=UNIT) #Arranque
        
rq = client.write_registers(9000, [6, 77, 83, 77, 48, 48, 48], unit=UNIT) #Terminar

rr = client.read_holding_registers(9001, 1, unit=UNIT)#Leemos los registros

        
        

for i in range(0, len(rr.registers)):
         print(i," ",rr.registers[i])

#time.sleep(2)
   


client.close()
    
#/////////Conexion pruebas