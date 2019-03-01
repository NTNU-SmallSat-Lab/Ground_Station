clear all
clc


FID = fopen("receive_complex.bin"); % import IQ from TX block
if FID == -1, error('Cannot open file'); end
Datastring=fread(FID,'single');   % By default, fread reads a file 1 byte at a time, interprets each byte as an 8-bit unsigned integer (uint8), and returns a double array.
fclose(FID);

for i=2:2:size(Datastring)-1
    p=i/2;
    IQ(p) = complex(Datastring(i),Datastring(i+1));
end


FID = fopen("complex_binary_feed.bin"); % import byte stream from TX block
if FID == -1, error('Cannot open file'); end
Datastring=fread(FID,'single');   % By default, fread reads a file 1 byte at a time, interprets each byte as an 8-bit unsigned integer (uint8), and returns a double array.
fclose(FID);

TX_data=Datastring;

FID = fopen("receive_float.bin"); % import byte stream from TX block
if FID == -1, error('Cannot open file'); end
Datastring=fread(FID,'single');   % By default, fread reads a file 1 byte at a time, interprets each byte as an 8-bit unsigned integer (uint8), and returns a double array.
fclose(FID);

RX_data=Datastring;

%for i=2:2:size(Datastring)-1
%    p=i/2;
%    data_IQ(p) = complex(Datastring(i),Datastring(i+1));
%end

%figure(1)
%subplot(2,1,1)
%plot(abs(IQ))
%plot(real(IQ))
%hold
%plot(imag(IQ))
%grid

%subplot(2,1,2)
%plot(real(data_IQ)%
%grid

figure(1)
subplot(2,1,1)
plot(TX_data) % (1:1199)
grid
legend('TX data')
subplot(2,1,2)
stem(RX_data(1:1199))
legend('RX data')
%plot(real(IQ(1000:1299))) % (1000:1100)
%plot(imag(IQ(1000:1299))
grid

figure(2)
%plot(TX_data(1000:1099)) % (1000:1100)
hold
plot(abs(IQ(1000:1199))) % (1000:1100)
%plot((IQ(1000:1099)))
legend('RX abs','RX imag') % 'TX data',
grid

