clear all
clc


FID = fopen("output.bin"); % import IQ from TX block
if FID == -1, error('Cannot open file'); end
Datastring=fread(FID,'single');   % By default, fread reads a file 1 byte at a time, interprets each byte as an 8-bit unsigned integer (uint8), and returns a double array.
fclose(FID);

for i=2:2:size(Datastring)-1
    p=i/2;
    IQ(p) = complex(Datastring(i),Datastring(i+1));
end


FID = fopen("byte_output.bin"); % import byte stream from TX block
if FID == -1, error('Cannot open file'); end
Datastring=fread(FID,'uint8');   % By default, fread reads a file 1 byte at a time, interprets each byte as an 8-bit unsigned integer (uint8), and returns a double array.
fclose(FID);

random_byte=Datastring;

figure(1)
subplot(2,1,1)
%plot(abs(IQ))
plot(real(IQ))
hold
plot(imag(IQ))
grid

subplot(2,1,2)
stem(random_byte)
grid

