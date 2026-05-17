import asyncio
import telnetlib3

async def main():
    reader, writer = await telnetlib3.open_connection("192.168.31.12", 23)
    
    try:
        writer.write("admin\n")
        writer.write("cisco123\n")
        await asyncio.sleep(1)

        writer.write("en\n")
        await asyncio.sleep(1)

        writer.write("cisco\n")
        await asyncio.sleep(1)

        writer.write("conf t\n")
        await asyncio.sleep(1)
        
        writer.write("hostname ROUTER1\n")
        await asyncio.sleep(1)
        
        writer.write("exit\n")
        await asyncio.sleep(1)
        
        writer.write("exit\n")  
        
        await asyncio.sleep(1)
        output = await reader.read()
        if output:
            print(output)
            
    except asyncio.TimeoutError:
        print("Timeout waiting for device response")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        writer.close()
        await writer.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())
