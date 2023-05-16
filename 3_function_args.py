# positional args
def positional_args(a, b, c):
    print(f'a={a}, b={b}, c={c}')


positional_args(1, 3, 'some')


# named args
#
# def positional_args(a, b, c: str = None):
#     print(f'a={a}, b={b}, c={c}')
#
#
# positional_args(a=2, b=1, c='some')
# positional_args(b=1, a=2, c='some')

# *args, **kwargs

# def func_args_kwargs(*args):
#     print(f'args={args}')
#     # kwargs.get('some')
#     # print(f'kwargs={kwargs}')


# func_args_kwargs(1, 2, 3)
# func_args_kwargs(k=123, v='some')

# unpacking
# config = {'host': '127.0.0.1', 'port': 6435, 'topic_name': 'something.something'}
#
#
# def kafka_client(host: str, port: int, topic_name: str):
#     print(f'Configured {host}:{port}')
#
#
# # kafka_client(host=config.get('host'), port=config.get('port'), topic_name=config.get('topic_name'))
#
# kafka_client(**config)
