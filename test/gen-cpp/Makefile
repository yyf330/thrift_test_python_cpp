BOOST_DIR = /usr/local/boost/include/boost-1_33_1/
THRIFT_DIR = /usr/include/thrift
LIB_DIR = /usr/local/lib
cc=g++
exe=server
obj=ProcessCheckL_server.o begenerallib.o besencryptf.o ProcessCheckL.o checklicense_constants.o checklicense_types.o

$(exe):$(obj)
	$(cc) -o $(exe) $(obj) -I${THRIFT_DIR} -I${BOOST_DIR}  -I../gen-cpp -L${LIB_DIR} -lthrift -lssl -lcrypto
		
ProcessCheckL_server.o:ProcessCheckL_server.cpp
	$(cc) -c ProcessCheckL_server.cpp
		
begenerallib.o:begenerallib.cpp
	$(cc) -c begenerallib.cpp
		
besencryptf.o:besencryptf.cpp
	$(cc) -c besencryptf.cpp
		
ProcessCheckL.o:ProcessCheckL.cpp
	$(cc) -c ProcessCheckL.cpp	
		
checklicense_constants.o:checklicense_constants.cpp
	$(cc) -c checklicense_constants.cpp
		
checklicense_types.o:checklicense_types.cpp
	$(cc) -c checklicense_types.cpp

		
clean:
	rm -rf *.o 
	rm -rf server 
