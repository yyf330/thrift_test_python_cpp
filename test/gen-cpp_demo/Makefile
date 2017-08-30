BOOST_DIR = /usr/local/boost/include/boost-1_33_1/
THRIFT_DIR = /usr/include/thrift
LIB_DIR = /usr/local/lib
cc=g++
exe=server
obj=UserStorage_server.o begenerallib.o besencryptf.o UserStorage.o demo_constants.o demo_types.o

$(exe):$(obj)
	$(cc) -o $(exe) $(obj) -I${THRIFT_DIR} -I${BOOST_DIR}  -I../gen-cpp -L${LIB_DIR} -lthrift -lssl -lcrypto
		
UserStorage_server.o:UserStorage_server.cpp
	$(cc) -c UserStorage_server.cpp
		
begenerallib.o:begenerallib.cpp
	$(cc) -c begenerallib.cpp
		
besencryptf.o:besencryptf.cpp
	$(cc) -c besencryptf.cpp
		
UserStorage.o:UserStorage.cpp
	$(cc) -c UserStorage.cpp	
		
demo_constants.o:demo_constants.cpp
	$(cc) -c demo_constants.cpp
		
demo_types.o:demo_types.cpp
	$(cc) -c demo_types.cpp

		
clean:
	rm -rf *.o 
	rm -rf server 
