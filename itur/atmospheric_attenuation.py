def compute_atmospheric_attenuation(
    p,

):
    if np.logical_or(p < 0.001, p > 50).any():
        warnings.warn(
            RuntimeWarning(
                "The method to compute the total "
                "atmospheric attenuation in recommendation ITU-P 618-13 "
                "is only recommended for unavailabilities (p) between "
                "0.001% and 50 %"
            )
        )
    
    # This takes account of the fact that a large part of the cloud attenuation
    # and gaseous attenuation is already included in the rain attenuation
    # prediction for time percentages below 1%. Eq. 64 and Eq. 65 in
    # Recommendation ITU 618-12
    p_c_g = np.maximum(1, p)

    


