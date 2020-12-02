
import math

PATH_LOSS_OFFSET = (20 * math.log(2.4, 10)) + 92.45

def calculate_path_loss_db(d_meters):
	'''
	Calculate the free space path loss for a transmission `d` meters.

	The return value is in decibels.
	'''


	# free space path loss found from provided resources
	d_kilos = d_meters / 1000
	return (20 * math.log(d_kilos, 10)) + PATH_LOSS_OFFSET



def calculate_snr_db(tx_power_db, path_loss_db, noise_db):
	'''
	Calculate the signal-to-noise ratio at the receiver based on
	the transmit power, the path loss, and the noise at the receiver.

	All values, including the return value, are in decibels.
	'''


	return tx_power_db - path_loss_db - noise_db


