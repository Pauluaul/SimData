import numpy as np

def rotate(Xorg, Yorg, Zorg, alpha, beta,
           gamma):
    X_ = Xorg * (np.cos(beta) * np.cos(gamma)) + \
         Yorg * (np.sin(alpha) * np.sin(beta) * np.cos(gamma) - np.cos(alpha) * np.sin(gamma)) + \
         Zorg * (np.cos(alpha) * np.sin(beta) * np.cos(gamma) + np.sin(alpha) * np.sin(gamma))
    # Yaw
    Y_ = Xorg * (np.cos(beta) * np.sin(gamma)) + \
         Yorg * (np.sin(alpha) * np.sin(beta) * np.sin(gamma) + np.cos(alpha) * np.cos(gamma)) + \
         Zorg * (np.cos(alpha) * np.sin(beta) * np.sin(gamma) - np.sin(alpha) * np.cos(gamma))
    # Pitch
    Z_ = Xorg * (-np.sin(beta)) + \
         Yorg * (np.sin(alpha) * np.cos(beta)) + \
         Zorg * (np.cos(alpha) * np.cos(beta))
    # roll
    return X_, Y_, Z_
