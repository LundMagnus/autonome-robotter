include libraries

fun DTMFsend(code) #function to send DTMF tones
	"send DTMF"
	
fun DTMFreceive()
	"receive and interpret DTMF tone"
	
setup
	DTMFsend("pound-symbol") # send wake-up command with DTMFsend function
	DTMFreceive() # Receive ACK with DTMFreceive function
	DTMFsend("some movement block") # Send a movement attempt in a DTMF 'block', either with algorithm or human made
	DTMFreceive() # Receive ACK and repeated command with DTMFreceive function
	DTMFsend("ACK")

main loop()

	#check whether the path chosen was good or bad
	DTMFreceive()
	if("bumped into wall")
		"tell the robot to forget the previous movement block and retry with a different movement block"
		DTMFsend("some movement block") # Send a movement attempt in a DTMF 'block', either with algorithm or human made
		DTMFreceive() # Receive ACK and repeated command with DTMFreceive function
		DTMFsend("ACK")
	else()
		"send a new movement block, that gets added to the previous block(s)"
		DTMFsend("some movement block") # Send a movement attempt in a DTMF 'block', either with algorithm or human made
		DTMFreceive() # Receive ACK and repeated command with DTMFreceive function
		DTMFsend("ACK")
	