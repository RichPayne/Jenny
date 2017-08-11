# Jenny

A scalable Python based Mirai honeypot built for easy setup & use.

## Requirements

* Python 2.7

## Usage

To run the listener 
```
python run.py
```

To run the c2 
```
python c2.py
```


## Future features

* Capture attempted commands executed
* Extract loader server IP 

## Known issues

* socket.error: [Errno 98] Address already in use
```
Solution: sudo fuser -k 23/tcp
```

## Authors

Richard Payne, 3rd year Cyber security student.

```
@TheRichPayne
```

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

