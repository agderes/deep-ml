import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
	
	grad = np.asarray(gradient, dtype=float)
	maginitude = np.linalg.norm(grad)
	if maginitude == 0:
		direction = np.zeros_like(grad)
	else:
		direction = grad / maginitude

	descent_direction = -direction
	
	return {"magnitude": maginitude, "direction": direction.tolist(), "descent_direction": descent_direction.tolist()}