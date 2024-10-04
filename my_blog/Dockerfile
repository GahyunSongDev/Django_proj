FROM python:3.12.2-slim

# copy the entire folder 
COPY . /app
# working directory is this /app folder
WORKDIR /app 

#run the virtual environment creation
RUN python3 -m venv venv /opt/virt

RUN /opt/virt/bin/pip install pip --upgrade && \
    /opt/virt/bin/pip install -r requirements.txt && \
    chmod +x entrypoint.sh

# entrypoint.sh 
CMD ["/app/entrypoint.sh"]