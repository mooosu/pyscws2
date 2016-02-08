PY_INCLUDE_DIR=/usr/include/python2.7
SCWS_INCLUDE_DIR=/usr/local/scws/include
SCWS_LIB_DIR=/usr/local/scws/lib

all: pyscws.c
	gcc pyscws.c -shared -o scws.so -I${PY_INCLUDE_DIR} -I${SCWS_INCLUDE_DIR} -L${SCWS_LIB_DIR} -lscws 
clean:
	rm scws.so
