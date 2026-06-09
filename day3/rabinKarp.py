#STRING MATCHING using RabinKarp's matching algorithm 

#KEY TAKEAWAY: RABIN KARP 
def rabin_karp(text, pattern):
      n, m, q = len(text), len(pattern), 101
      p_hash = t_hash = 0
      h = pow(10, m - 1, q)

      for i in range(m):
          p_hash = (10 * p_hash + ord(pattern[i])) % q
          t_hash = (10 * t_hash + ord(text[i])) % q
          
      for i in range(n - m + 1):
          if p_hash == t_hash and text[i:i+m] == pattern:
              print(f"Match at index {i}")
          if i < n - m:
              t_hash = (10 * (t_hash - ord(text[i]) * h) + ord(text[i+m])) % q
              t_hash %= q
  
rabin_karp("45123", "123")