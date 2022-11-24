class RSA:
    @classmethod
    def __is_prime(cls, number: int) -> bool:
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
        
        mod = (lambda p, q: p * q if cls.__is_prime(p) and cls.__is_prime(q) else None)(p, q)
        
        e = exp[0] if exp[0] != mod else exp[-1]
        return (e, mod, fi) if mod else None
        
    @classmethod
    def __gen_keys(cls, p: int, q: int) -> tuple:
        e, mod, fi = cls.__func_eler(p, q)
        d : int = 0
        while (d * e) % fi != 1: 
            d += 1
            if d == e:
                d += 1
        
        public_key = (e, mod)
        private_key = (d, mod)
        print(e, fi, mod, d)
        
        return public_key, private_key
        
    @classmethod
    def encode(cls, *, message: int, p_q: list):
        public_key, _ = cls.__gen_keys(*p_q)
        e, mod = public_key
        if message < mod:
            msg = message ** e
            return msg % mod
        else:
            raise ValueError('[!] Mesasge is very long')
    
    @classmethod
    def decode(cls, *, msg: int, p_q: list):
        _, private_key = cls.__gen_keys(*p_q)
        d, mod = private_key
        message = msg ** d
        return message % mod
        
