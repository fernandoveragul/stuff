# Код заимствован у zopefoundation/roman/blob/master/src/roman.py

class RomanNumeric:
    ROMINT: tuple = [
        ('M', 1000),
        ('CM', 900),
        ('D', 500),
        ('CD', 400),
        ('C', 100),
        ('XC', 90),
        ('L', 50),
        ('XL', 40),
        ('X', 10),
        ('IX', 9),
        ('V', 5),
        ('IV', 4),
        ('I', 1)
        ]
    
    @classmethod
    def __validate_int_to_rom(cls, *, number: int):
        if not isinstance(number, int):
            return False 
        if not (-1 < number < 5000):
            return False  
        return True
    
    @classmethod
    def __validate_rom_to_int(cls, *, roman: str):
        if not roman:
            return False
        if not RomanNumeric.ROMINT.search(roman):
            return False
        return True
    
    @classmethod
    def convert_rom_to_int(cls, roman: str = None) -> int:
        if roman == 'N':
            return 0
            
        if RomanNumeric.__validate_rom_to_int(roman=roman):
            result = 0
            index = 0
            for numeral, integer in RomanNumeric.ROMINT:
                while s[index:index + len(numeral)] == numeral:
                    result += integer
                    index += len(numeral)
            return result
        else:
            return -1
        
    @classmethod
    def convert_int_to_rom(cls, number: int) -> str:
        if number == 0:
            return 'N'
            
        if RomanNumeric.__validate_int_to_rom(number=number):
            result = ""
            for roman, integer in RomanNumeric.ROMINT:
                while number >= integer:
                    result += roman
                    number -= integer
            return result
        else:
            return 'ERROR'
