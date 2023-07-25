from plates import is_valid


def all_alnum(): 

    assert is_valid('sweet') == True
    assert is_valid('cs50') == True
    assert is_valid('glam') == True
    assert is_valid('gas') == True
    assert is_valid('lk11') == True

    assert is_valid('swee.t') == False   
    assert is_valid('cs50.') == False
    assert is_valid('cs|50') == False
    assert is_valid('glam!') == False
    assert is_valid('gas?') == False
    assert is_valid('whyme?') == False
    assert is_valid('no_gas') == False
    assert is_valid('l0_0l') == False
    assert is_valid('[mine]') == False


def length():

    assert is_valid('sd') == True
    assert is_valid('sfg') == True
    assert is_valid('myname') == True
    assert is_valid('iamher') == True

    assert is_valid('c') == False
    assert is_valid('w') == False
    assert is_valid('hisname') == False
    assert is_valid('whythem') == False
    

def test_first_two_alpha():

    assert is_valid('qw') == True
    assert is_valid('am') == True
    assert is_valid('qwert') == True
    assert is_valid('amnot') == True

    assert is_valid('a3') == False
    assert is_valid('3t') == False
    assert is_valid('45') == False
    assert is_valid('a3wy') == False
    assert is_valid('50cs') == False
    assert is_valid('3guy') == False
    

def first_zero():

    assert is_valid('cs1') == True

    assert is_valid('csp1') == True
    assert is_valid('cs10') == True
    assert is_valid('cs11') == True

    assert is_valid('cspp1') == True
    assert is_valid('csp10') == True
    assert is_valid('csp11') == True
    assert is_valid('cs100') == True
    assert is_valid('cs101') == True
    assert is_valid('cs110') == True
    assert is_valid('cs111') == True

    assert is_valid('csppp1') == True
    assert is_valid('cspp10') == True
    assert is_valid('cspp11') == True
    assert is_valid('csp100') == True
    assert is_valid('csp101') == True
    assert is_valid('csp110') == True
    assert is_valid('csp111') == True
    assert is_valid('cs1000') == True
    assert is_valid('cs1001') == True
    assert is_valid('cs2010') == True
    assert is_valid('cs2100') == True
    assert is_valid('cs3101') == True
    assert is_valid('cs4111') == True

    assert is_valid('cs0') == False

    assert is_valid('csp0') == False
    assert is_valid('cs0') == False
    assert is_valid('cs01') == False

    assert is_valid('cspp0') == False
    assert is_valid('csp00') == False
    assert is_valid('csp01') == False
    assert is_valid('cs000') == False
    assert is_valid('cs001') == False
    assert is_valid('cs010') == False
    assert is_valid('cs011') == False

    assert is_valid('csppp0') == False
    assert is_valid('cspp00') == False
    assert is_valid('cspp01') == False
    assert is_valid('csp000') == False
    assert is_valid('csp001') == False
    assert is_valid('csp010') == False
    assert is_valid('csp012') == False
    assert is_valid('cs0000') == False
    assert is_valid('cs0001') == False
    assert is_valid('cs0010') == False
    assert is_valid('cs0100') == False
    assert is_valid('cs0101') == False
    assert is_valid('cs0123') == False

def last_alpha():
    assert is_valid('cs5') == True
    assert is_valid('csp') == True

    assert is_valid('cs50') == True
    assert is_valid('csp5') == True
    assert is_valid('cssp') == True

    assert is_valid('csp50') == True
    assert is_valid('csp500') == True
    assert is_valid('cspppp') == True
    assert is_valid('csppp1') == True
    assert is_valid('cspp10') == True
    assert is_valid('cspp12') == True
    assert is_valid('csp100') == True
    assert is_valid('csp102') == True
    assert is_valid('csp123') == True
    assert is_valid('cs1000') == True
    assert is_valid('cs1002') == True
    assert is_valid('cs1023') == True
    assert is_valid('cs1234') == True
   

    assert is_valid('cs5p') == False

    assert is_valid('csp0p') == False
    assert is_valid('csp1p') == False
    assert is_valid('cs0pp') == False
    assert is_valid('cs2pp') == False

    assert is_valid('cspp0p') == False
    assert is_valid('cspp1p') == False
    assert is_valid('csp0pp') == False
    assert is_valid('csp2pp') == False
    assert is_valid('cs0ppp') == False
    assert is_valid('cs3ppp') == False
    assert is_valid('csp00p') == False
    assert is_valid('csp40p') == False
    assert is_valid('cs00pp') == False
    assert is_valid('cs50pp') == False
    assert is_valid('csp0p0') == False
    assert is_valid('csp6p0') == False
    assert is_valid('cs0pp0') == False
    assert is_valid('cs7pp0') == False
    assert is_valid('cs0p0p') == False
    assert is_valid('cs8p0p') == False
    assert is_valid('cs000p') == False
    assert is_valid('cs800p') == False
    assert is_valid('cs00p0') == False
    assert is_valid('cs20p0') == False
    assert is_valid('cs0p00') == False
    assert is_valid('cs5p00') == False