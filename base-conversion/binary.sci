clear
clc

k = 1;

N(k) = 30;
//vetor com o nome n. k é a posição que o elemento ocupa no vetor

p = 0;

while p == 0
  quociente = N(k)/2;
  q(k) = int(quociente);
  r(k) = N(k) - 2*q(k) ;//resto da divisão
  a(k) = r(k);
  
  if q(k) == 0 then
  	p = 1;
    
  else
    N(k+1) = q(k);
    k = k + 1;
  end
end

for i = 1:k
	b(i) = a(k-i+1);
end

disp(b)
