--parte 1
f x = case x of
 	0 -> 1
 	1 -> 5
 	2 -> 2
 	_ -> 1

quicksort :: (Ord a) => [a] -> [a]
quicksort [] = []
quicksort (x:xs) = quicksort lt ++ [x] ++ quicksort ge where {lt = [y | y <- xs, y < x]; ge = [y | y <- xs, y >= x]}

--parte 2
--normal
lista = [1..1000]
pa = [1,3..99]
pg = [2^x| x<-[1..50]]
fat x = product [1..x]
--lambda
fatorial n= map(\x->product [1..x]) [1..] !!n
listaLamb = map(\x->x) [1..1000]
paLamb = [x | x<-map(\x->1+3*x)[0..99], x < 100]
pgLamb = map(\x-> 2^x) [1..50]