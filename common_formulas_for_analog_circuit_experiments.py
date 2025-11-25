from math import inf

def common_emitter_amplifier_circuit_A_v(beta,R_C,R_L,I_EQ,Y_T=26e-3,r_bb=200):
    """
    Calculate the voltage gain (A_v) of a common-emitter amplifier circuit.
    Parameters:
    beta (float): Current gain of the transistor.
    R_C (float): Collector resistor in ohms.
    R_L (float): Load resistor in ohms.
    I_EQ (float): Quiescent emitter current in amperes.
    Y_T (float): Thermal voltage in millivolts (default is 26 mV).
    r_bb (float): Base spreading resistance in ohms (default is 200 ohms).
    Returns:
    float: Voltage gain (A_v) of the common-emitter amplifier circuit.
    """
    r_e = Y_T / I_EQ  # Emitter resistance
    r_be = r_bb + (beta + 1) * r_e  # Base-emitter resistance
    if R_L!=inf:
        R_L_=(R_C*R_L)/(R_C+R_L) # Combined load resistance
    elif R_L==inf:
        R_L_=R_C
    A_v = -beta * R_L_ / r_be
    return A_v

def common_collector_amplifier_circuit_A_v(beta,R_E,R_L,I_EQ,Y_T=26e-3,r_bb=200):
    """
    Calculate the voltage gain (A_v) of a common-collector amplifier circuit.
    Parameters:
    beta (float): Current gain of the transistor.
    R_E (float): Emitter resistor in ohms.
    R_L (float): Load resistor in ohms.
    I_EQ (float): Quiescent emitter current in amperes.
    Y_T (float): Thermal voltage in millivolts (default is 26 mV).
    r_bb (float): Base spreading resistance in ohms (default is 200 ohms).
    Returns:
    float: Voltage gain (A_v) of the common-collector amplifier circuit.
    """
    r_e = Y_T / I_EQ  # Emitter resistance
    r_be = r_bb + (beta + 1) * r_e  # Base-emitter resistance
    if R_L!=inf:
        R_L_=(R_E*R_L)/(R_E+R_L) # Combined load resistance
    elif R_L==inf:
        R_L_=R_E
    A_v=(1+beta)*R_L_/(r_be+(1+beta)*R_L_)
    return A_v

def common_collector_amplifier_circuit_R_input(beta,R_E,R_B,R_L,I_EQ,Y_T=26e-3,r_bb=200):
    """
    Calculate the input resistance (R_i) of a common-collector amplifier circuit.
    Parameters:
    beta (float): Current gain of the transistor.
    R_E (float): Emitter resistor in ohms.
    R_B (float): Base resistor in ohms.
    R_L (float): Load resistor in ohms.
    I_EQ (float): Quiescent emitter current in amperes.
    Y_T (float): Thermal voltage in millivolts (default is 26 mV).
    r_bb (float): Base spreading resistance in ohms (default is 200 ohms).
    returns:
    float: Input resistance (R_i) of the common-collector amplifier circuit.
    """
    r_e = Y_T / I_EQ  # Emitter resistance
    r_be = r_bb + (beta + 1) * r_e  # Base-emitter resistance
    if R_L!=inf:
        R_L_=(R_E*R_L)/(R_E+R_L) # Combined load resistance
    elif R_L==inf:
        R_L_=R_E
    r_x=r_be+(1+beta)*R_L_
    r_i=(R_B*r_x)/(R_B+r_x)
    return r_i

def common_collector_amplifier_circuit_R_output(beta,R_E,R_B,R_S,I_EQ,Y_T=26e-3,r_bb=200):
    """
    Calculate the output resistance (R_o) of a common-collector amplifier circuit.
    Parameters:
    beta (float): Current gain of the transistor.
    R_E (float): Emitter resistor in ohms.
    R_B (float): Base resistor in ohms.
    R_S (float): Source resistor in ohms.
    I_EQ (float): Quiescent emitter current in amperes.
    Y_T (float): Thermal voltage in millivolts (default is 26 mV).
    r_bb (float): Base spreading resistance in ohms (default is 200 ohms).
    Returns:
    float: Output resistance (R_o) of the common-collector amplifier circuit.
    """
    r_e = Y_T / I_EQ  # Emitter resistance
    r_be = r_bb + (beta + 1) * r_e  # Base-emitter resistance
    if R_S!=inf:
        R_S_=(R_B*R_S)/(R_B+R_S) # Combined source resistance
    elif R_S==inf:
        R_S_=R_B
    r_x=(r_be+R_S_)/(1+beta)
    r_o=(R_E*r_x)/(R_E+r_x)
    return r_o

def common_base_amplifier_circuit_A_v(beta,R_C,R_L,I_EQ,Y_T=26e-3,r_bb=200):
    """
    Calculate the voltage gain (A_v) of a common-base amplifier circuit.
    Parameters:
    beta (float): Current gain of the transistor.
    R_C (float): Collector resistor in ohms.
    R_L (float): Load resistor in ohms.
    I_EQ (float): Quiescent emitter current in amperes.
    Y_T (float): Thermal voltage in millivolts (default is 26 mV).
    r_bb (float): Base spreading resistance in ohms (default is 200 ohms).
    Returns:
    float: Voltage gain (A_v) of the common-base amplifier circuit.
    """
    r_e = Y_T / I_EQ  # Emitter resistance
    r_be = r_bb + (beta + 1) * r_e  # Base-emitter resistance
    if R_L!=inf:
        R_L_=(R_C*R_L)/(R_C+R_L) # Combined load resistance
    elif R_L==inf:
        R_L_=R_C
    A_v = beta * R_L_ / r_be
    return A_v