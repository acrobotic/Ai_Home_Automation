import spi

status = spi.openSPI(speed=500000)
print "SPI configuration = ", status

print "Reading from Arduinos:"

dat = spi.transfer((1,3,5))
for i in range(len(dat)):
    print dat[i]

spi.closeSPI()
