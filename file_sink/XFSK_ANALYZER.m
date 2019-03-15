clear all
clc

FID = fopen("Receive_Complex_Waveform.bin"); % import from File Dump
if FID == -1, error('Cannot open file'); end
Datastring=fread(FID,'single');   % Create array of single precision floating point
fclose(FID);

for i=2:2:size(Datastring)-1 % Assemble couplex single (IQ) array from complex double 
    p=i/2;
    IQ(p) = complex(Datastring(i),Datastring(i+1));
end

RX_Complex_Waveform=IQ;

FID = fopen("complex_binary_feed.bin"); % import byte stream from TX block
if FID == -1, error('Cannot open file'); end
Datastring=fread(FID,'single');   % Create array of single precision floating point
fclose(FID);

TX_data=Datastring;

FID = fopen("receive_float.bin"); % import from File Dump
if FID == -1, error('Cannot open file'); end
Datastring=fread(FID,'single');   % Create array of single precision floating point
fclose(FID);

RX_data=Datastring;

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
plot(RX_data)
legend('RX data')
%plot(real(IQ(1000:1299))) % (1000:1100)
%plot(imag(IQ(1000:1299))
grid

figure(2)
plot(real(RX_Complex_Waveform(1:100))) % (1000:1100)
hold on
plot(imag(RX_Complex_Waveform(1:100))) % (1000:1100)
legend('Received waveform (I)','Received waveform (Q)')
grid

