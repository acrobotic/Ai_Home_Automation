import spi

status = spi.openSPI(speed=1000000)
print "SPI configuration = ", status

print "Reading from Arduinos:"

dat = spi.transfer((1,3,5,6))
for i in range(len(dat)):
    print dat[i]

spi.closeSPI()
