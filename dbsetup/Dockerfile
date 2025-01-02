# Base image with Oracle Database
FROM gvenzl/oracle-xe:21-slim as oracle

# Install Python and required packages in the container
RUN apt-get update && apt-get install -y python3 python3-pip libaio1

# Set environment variables for Oracle
ENV ORACLE_HOME=/opt/oracle/product/21c/dbhomeXE
ENV PATH=$ORACLE_HOME/bin:$PATH
ENV LD_LIBRARY_PATH=$ORACLE_HOME/lib:$LD_LIBRARY_PATH

# Set up working directory
WORKDIR /app

# Copy application files (Python script and CSV)
COPY queries.py data.csv ./

# Install Python dependencies
RUN pip3 install pandas cx_Oracle

# Expose Oracle database and Python app ports (optional)
EXPOSE 1521 5500

# Start Oracle DB and run Python script
CMD ["sh", "-c", "/opt/oracle/runOracle.sh && sleep 10 && python3 queries.py"]
