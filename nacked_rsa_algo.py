class RSA:
    @classmethod
    def __is_prime(cls, number: int) -> bool:
        """This function check : number is prime?"""
        
        i = 1
        a = []
        while i ** 2 <= number:
            if number % i == 0:
                a.append(i)
                if i != number // i:
                    a.append(number // i)
            i += 1
        if len(a) == 2:
            return True
        else:
            return False
            
    @classmethod
    def __func_eler(cls, p: int, q: int) -> tuple:
        """Function of Eler is {(p - 1) * (q - 1)}"""
        
        fi = (p - 1) * (q - 1)
        exp = [i for i in range(fi) if cls.__is_prime(i) and fi % i != 0]
        mod = (lambda p, q: p * q if all(list(map(cls.__is_prime, [p, q]))) else None)(p, q)
        e = exp[-1]
        return (e, mod, fi) if mod else None
        
    @classmethod
    def __gen_keys(cls, p: int, q: int) -> tuple:
        """This function generate and return (public_key, private_key)"""
        
        e, mod, fi = cls.__func_eler(p, q)
        d: int = 0
        while (d * e) % fi != 1: 
            d += 1
            if d == e:
                d += 1
        public_key = (e, mod)
        private_key = (d, mod)
        return public_key, private_key
        
    @classmethod
    def encode(cls, *, message: int, p_q: list) -> int:
        if public_key := cls.__gen_keys(*p_q)[0]:
            e, mod = public_key 
            if message < mod:
                return (message ** e) % mod
            else:
                raise ValueError('[!] Mesasge is very long')
        else:
            raise ValueError('[!] Public key is empty!')
        
    @classmethod
    def decode(cls, *, message: int, p_q: list) -> int:
        if private_key := cls.__gen_keys(*p_q)[-1]:
            d, mod = private_key
            return (message ** d) % mod
        else:
            raise ValueError('[!] Private key is empty!')
            
