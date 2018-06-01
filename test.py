from boltiot.bolt import Bolt
import unittest
import json
import time

client = Bolt('7bc48b25-f5c8-4ef3-9477-c599835583da','BOLT3729610') # Pass in the API Key and the client ID.

class BoltTests(unittest.TestCase):
    
# Testing the digital write function.
    
    def test_1(self):
        assert_value = json.loads(client.digitalWrite('4','HIGH'))
        self.assertEqual(assert_value["success"],"1")
        self.assertEqual(assert_value["value"],"1")
        print("Digital Write Successfull!")

# Testing the analog write function
        
    def test_3(self):
        assert_value = json.loads(client.analogWrite('0','100'))
        self.assertEqual(assert_value["success"],"1")
        self.assertEqual(assert_value["value"],"1")
        print("Analog Write Successfull!")
        
# Testing the digital read function.
        
    def test_2(self):
        assert_value = json.loads(client.digitalRead('1'))
        self.assertEqual(assert_value["success"],"1")
        self.assertEqual(int(assert_value["value"]),1)
        print("Digital Read Successfull!")
        
# Testing the analog read function.
        
    def test_4(self):
        assert_value = json.loads(client.analogRead('A0'))
        self.assertEqual(assert_value["success"],"1")
        self.assertTrue(0 <= int(assert_value["value"]) <= 1024)
        print("Analog Read Succesfull!")
        
# Testing the serialBegin() function.
        
    def test_5(self):
        assert_value = json.loads(client.serialBegin("9600"))
        self.assertEqual(assert_value["success"],"1")
        self.assertEqual(assert_value["value"],"Success")
        print("Serial Begin Successfull!")
        
# Testing the serialWrite() function.
        
    def test_6(self):
        assert_value = json.loads(client.serialWrite('inventrom'))
        self.assertEqual(assert_value["success"],"1")
        self.assertEqual(assert_value["value"],"Serial write Successful")
        print("Serial Write Successfull!")
        
# Testing the serialRead() function.
        
    def test_7(self):
        assert_value = json.loads(client.serialRead('10'))
        self.assertEqual(assert_value["success"],"1")
        self.assertEqual(assert_value["value"],"inventrom")
        print("Serial Read Successfull!")
        
# Testing the restart() function.

    def test_restart(self):
        assert_value = json.loads(client.restart())
        time.sleep(5)
        try :
            self.assertEqual(assert_value["value"],"Restarted")
        except AssertionError:
            self.assertEqual(assert_value["value"], "Command timed out")
        print("Restart Successfull!")
        
# Testing the isAlive() function.
        
    def test_8(self):
        assert_value = json.loads(client.isAlive())
        self.assertEqual(assert_value["success"],"1")
        self.assertEqual(assert_value["value"],"alive")
        print("isAlive Successfull!")
        
# Testing the isOnline() function
        
    def test_9(self):
        assert_value = json.loads(client.isOnline())
        self.assertEqual(str(assert_value["success"]),"1")
        self.assertEqual(assert_value["value"],"online")
        print("isOnline Successfull!")

if __name__ == "__main__":
    device_status = json.loads(client.isOnline())
    if(device_status["value"] == "online"):
        unittest.main()
    else:
        print("The device is offline test cannot be conducted at the moment. Connect your Bolt to the cloud before testing it.")