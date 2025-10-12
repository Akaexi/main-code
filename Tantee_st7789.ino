#include <Adafruit_GFX.h>
#include <Adafruit_ST7789.h>
#include <SPI.h>

#define TFT_CS    -1
#define TFT_DC    2
#define TFT_RST   4

// wairing lcd ke esp32:
// vcc to 3,3v
// gnd to gnd
// scl to d18
// sda to d23

Adafruit_ST7789 tft = Adafruit_ST7789(TFT_CS, TFT_DC, TFT_RST);

String lirik[] = {
  "Tantee...",           
  "Sudah terbiasa terjadi tantee...",
  "Teman datang ketika lagi butuh sajaa~",
  "Coba kalau lagi susaahhhh~~",
  "Mereka semua menghilaaanggg.....",
  "by fadhil"
};

int jumlahLirik = sizeof(lirik) / sizeof(lirik[0]);

void setup() {
  tft.init(240, 240, SPI_MODE3);
  tft.setRotation(2);
  tft.fillScreen(ST77XX_BLACK);
  tft.setTextWrap(false);
  tft.setTextColor(ST77XX_WHITE);
}

void loop() {
  for (int i = 0; i < jumlahLirik; i++) {
    scrollKalimat(lirik[i], 3000);  // 3000 ms = 3 detik per lirik
    delay(35);                     // jeda antar kalimat
  }

  tampilkanCredit();
  while (true); // berhenti di akhir
}

void scrollKalimat(String text, int durasiMS) {
  int16_t y = 100;
  int16_t x = 240;
  int16_t textWidth = text.length() * 18;  // kira-kira lebar teks font 
  int16_t prevX = x;

  tft.fillScreen(ST77XX_BLACK);
  tft.setTextSize(3);

  int totalGerak = x + textWidth;  // total jarak dari kanan keluar kiri
  int langkah = 4;                 // piksel per frame
  int totalFrame = totalGerak / langkah;
  int delayPerFrame = durasiMS / totalFrame; // hitung otomatis biar durasi sama

  while (x + textWidth > 0) {
    tft.fillRect(prevX, y - 5, textWidth + 10, 40, ST77XX_BLACK);
    tft.setCursor(x, y);
    tft.setTextColor(ST77XX_WHITE);
    tft.print(text);

    prevX = x;
    x -= langkah;
    delay(delayPerFrame);
  }

  tft.fillScreen(ST77XX_BLACK);
}

void tampilkanCredit() {
  tft.fillScreen(ST77XX_BLACK);
  tft.setTextColor(ST77XX_YELLOW);
  tft.setTextSize(3);
  tft.setCursor(30, 200);
  tft.print("Volcra.lab by fadhil");
}
