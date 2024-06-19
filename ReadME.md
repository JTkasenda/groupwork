Hi guys, this is how to excute this app.

Prerequisites:
================================================================
- Install Celery

    pip install celery

- Install PIL

    pip install pillow 

-Install gevent

    pip install gevent

-Install RabbitMQ server or use  RabbitMQ image from docker


1. Start your RabbitMQ server

    - Try the docker image(Of RabbitMq) first, if it doesn't exist work

    - Download the windows native RabbitMq server app (Don't forget Erlang lol)

    NB: Don't forget to bind the ports if you are using a docker image

    example: docker run -d -p 5672:5672 -p 15672:15672 --name rabbitmq rabbitmq:management

2. Start your Celery worker with the following command

    bash celery -A tpCelery1.work worker -l info -P  gevent

3. Start your main file in this case (run.py) and watch the magic