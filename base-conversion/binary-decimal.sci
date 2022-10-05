clear clc

r(1) = 0.4375;
parada = 100;
k = 1;
p = 0;

// ok

while p == 0
  calc = 2*r(k);
  if calc >= 1 then
  	d(k) = 1;
  else
    d(k) = 0;
  end
  
  r(k+1) = calc - d(k);
  
  if r(k+1) == 0 then
  	p = 1;
  else
    k = k + 1;
  
  if k > parada then
  	p = 1
  end
  
 end
 
end

disp(d);