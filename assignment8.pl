:-initialization(main).
main :- write('AIRLINE MANAGEMENT SYSTEM').

place('toronto',1).
place('london',2).
place('barcelona',3).
place('madrid',4).
place('malaga',5).
place('paris',6).
place('toulouse',7).
place('valencia',8).

air('toronto','$50',60).
air('madrid','$75',45).
air('malaga','$50',30).
air('valencia','$40',20).
air('barcelona','$40',30).
air('london','$75',80).
air('paris','$50',60).
air('toulouse','$40',30).

route(1,aircanada,2,500,360).
route(1,united,2,650,420).
route(1,aircanada,4,900,480).
route(4,united,1,950,540).
route(1,iberia,4,800,480).
route(3,aircanada,4,100,60).
route(3,iberia,4,120,65).
route(8,iberia,4,40,50).
route(5,iberia,8,80,120).
route(7,united,6,35,120).
route(3,iberia,2,220,240).
route(3,iberia,8,110,75).
route(4,iberia,5,50,60).

flightdes(From,flight,To,Price,Duration):-(route(1,aircanada,2,500,360);reversepath(2,aircanada,1,500,360)),
nl,write('london aircanada toronto $50 60'),
nl,write('toronto aircanada london $50 60'),
(route(1,united,2,650,420);reversepath(2,united,1,650,420)),
nl,write('toronto united london $650 420'),
nl,write('london united toronto $650 420'),
(route(1,aircanada,4,900,480);reversepath(4,aircanada,1,900,480)),
nl,write('toronto aircanada madrid $900 480'),
nl,write('madrid aircanada toronto $900 480'),
(route(4,united,1,950,540);reversepath(1,united,4,950,540)),
nl,write('madrid united toronto $950 540'),
nl,write('toronto united madrid $950 540'),
(route(1,iberia,4,800,480);reversepath(4,iberia,1,800,480)),
nl,write('toronto iberia madrid $800 480'),
nl,write('madrid iberia toronto $800 480'),
(route(3,aircanada,4,100,60);reversepath(4,aircanada,3,100,60)),
nl,write('barcelona aircanada madrid $100 60'),
nl,write('madrid aircanada barcelona $100 60'),
(route(3,iberia,4,120,65);reversepath(4,iberia,3,120,65)),
nl,write('barcelona iberia madrid $120 65'),
nl,write('madrid iberia barcelona $120 65'),
(route(8,iberia,4,40,50);reversepath(4,iberia,8,40,50)),
nl,write('valencia iberia madrid $40 50'),
nl,write('madrid iberia valencia $40 50'),
(route(5,iberia,8,80,120);reversepath(8,iberia,5,80,120)),
nl,write('malaga iberia valencia $80 120'),
nl,write('valencia iberia malaga $80 120'),
(route(7,united,6,35,120);reversepath(6,united,7,35,120)),
nl,write('toulese iberia paris $35 120'),
nl,write('paris iberia toulouese $35 120'),
(route(3,iberia,2,220,240);reversepath(2,iberia,3,220,240)),
nl,write('london iberia barcelona $220 240'),
nl,write('barcelona iberia london $220 240'),
(route(3,iberia,8,110,75);reversepath(8,iberia,3,110,75)),
nl,write('barcelona iberia valencia $110 75'),
nl,write('valencia iberia barcelona $110 75'),
(route(4,iberia,5,50,60);reversepath(5,iberia,4,50,60)),
nl,write('madrid iberia malaga $50 60'),
nl,write('malaga iberia madrid $50 60').

airport(city,airporttax,minsecuritydelay):-
air('toronto','$50',60),
nl,write('toronto $50 60'),
air('madrid','$75',45),
nl,write('madrid $75 45'),
air('malaga','$50',30),
nl,write('malaga $50 30'),
air('valencia','$40',20),
nl,write('valencia $40 20'),
air('barcelona','$40',30),
nl,write('london $75 80'),
air('paris','$50',60),
nl,write('paris $50 60'),
air('toulouse','$40',30),
nl,write('toulouse $40 30').

airline('iberia',1).
airline('aircanada',2).
airline('united',3).


	
/*1.Rules to get the flights from toronto to madrid*/
flight(From,X,To,Z,W):-place(From,A),place(To,B),(route(A,X,B,Y,Z);route(B,X,A,Y,Z)).

/*2.Rules to get the flights with price less than 400*/
price(From,C,To):-place(From,A),place(To,B),(route(A,C,B,X,Y);route(B,C,A,X,Y)),X<400.

/*3.Is it possible to go in two flights*/
twoflights(toronto,paris):-route(1,X,C,Y,Z),route(C,F,6,A,B).

/*4.Cheap or airline is airline is aircanada*/
prefer(From,C,To):-price(From,C,To);(place(From,A),place(To,B),(route(A,C,B,X,_);route(B,C,A,X,_)),C=aircanada,X>400).

/*5.If there is a flight from A to B through United Airline then there is a flight using airCanada as well*/
possible(From,To):-place(From,A),place(To,B),route(A,united,B,_,_)->route(A,aircanada,B,_,_).


