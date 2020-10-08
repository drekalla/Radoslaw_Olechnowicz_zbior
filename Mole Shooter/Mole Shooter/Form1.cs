#define My_Debug

using Mole_Shooter.Properties;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Media;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Mole_Shooter
{
    public partial class MoleShooter : Form
    {
        Form2 f = new Form2();
        const int FrameNum = 8;

        const int SplatNum = 3;

        bool splat = false;

        int _gameFrame = 0;
        int _splatTime = 0;

        int _hits = 0;
        int _misses = 0;
        int _totalShots = 0;
        double _averageHits = 0;

#if My_Debug
        int _cursX = 0;
        int _cursY = 0;
#endif
        CMole _mole;
        CSplat _splat;
        CSign _sign;
        CScoreFrame _scoreframe;

        Random rnd = new Random();

        public MoleShooter()
        {
            InitializeComponent();

            Bitmap b = new Bitmap(Resources.Site);
            this.Cursor = CustomCursor.CreateCursor(b, b.Height / 2, b.Width / 2);

            _scoreframe = new CScoreFrame() { Left = 10, Top = 10 };
            _sign = new CSign() { Left = 340, Top = 10 };
            _mole = new CMole() { Left = 10, Top = 200 };
            _splat = new CSplat();
        }

        private void timerGameLoop_Tick(object sender, EventArgs e)
        {
            if (_gameFrame >= FrameNum)
            {
                UpdateMole();
                _gameFrame = 0;
            }

            if(splat)
            {
                if(_splatTime >= SplatNum)
                {
                    splat = false;
                    _splatTime = 0;
                    UpdateMole();
                }
                _splatTime++;
            }

            _gameFrame++;
            this.Refresh();
        }

        private void UpdateMole()
        {
            _mole.Update(
                rnd.Next(Resources.Mole.Width, this.Width - Resources.Mole.Width),
                rnd.Next(this.Height / 2, this.Height - Resources.Mole.Height * 2));
        }

        protected override void OnPaint(PaintEventArgs e)
        {
            Graphics dc = e.Graphics;

            if (splat == true)
            {
                _splat.DrawImage(dc);
            }
            else
            {
                _mole.DrawImage(dc);
            }

            

            _sign.DrawImage(dc);
            _scoreframe.DrawImage(dc);

#if My_Debug
            TextFormatFlags flags = TextFormatFlags.Left | TextFormatFlags.EndEllipsis;
            Font _font = new System.Drawing.Font("Stencil", 12, FontStyle.Regular);
            TextRenderer.DrawText(dc, "X=" + _cursX.ToString() + ":" + "Y=" + _cursY.ToString(), _font,
                new Rectangle(0, 0, 120, 20), SystemColors.ControlText, flags);
#endif
            /*
            TextFormatFlags flags = TextFormatFlags.Left;
            Font _font = new System.Drawing.Font("Stencil", 12, FontStyle.Regular);
            */
            TextRenderer.DrawText(e.Graphics, "Shots:" + _totalShots.ToString(), _font, new Rectangle(30, 32, 120, 20), SystemColors.ControlText, flags);
            TextRenderer.DrawText(e.Graphics, "Hits:" + _hits.ToString(), _font, new Rectangle(30, 52, 120, 20), SystemColors.ControlText, flags);
            TextRenderer.DrawText(e.Graphics, "Misses:" + _misses.ToString(), _font, new Rectangle(30, 72, 120, 20), SystemColors.ControlText, flags);
            TextRenderer.DrawText(e.Graphics, "Avg:" + _averageHits.ToString("F0") + "%", _font, new Rectangle(30, 92, 120, 20), SystemColors.ControlText, flags);

            base.OnPaint(e);
        }

        private void MoleShooter_MouseMove(object sender, MouseEventArgs e)
        {
#if My_Debug
            _cursX = e.X;
            _cursY = e.Y;
#endif
            this.Refresh();
        }

        private void MoleShooter_MouseClick(object sender, MouseEventArgs e)
        {
            if (e.X > 420 && e.X < 485 && e.Y > 65 && e.Y < 85)
            {
                timerGameLoop.Start();
            }
            else if (e.X >420 && e.X < 485 && e.Y > 90 && e.Y <105)
            {
                timerGameLoop.Stop();
                _hits = 0;
                _misses = 0;
                _totalShots = 0;
                _averageHits = 0;
            }
            else if (e.X > 420 && e.X < 485 && e.Y > 110 && e.Y < 130)
            {
                timerGameLoop.Stop();
                _hits = 0;
                _misses = 0;
                _totalShots = 0;
                _averageHits = 0;
                f.Show();

            }
            else if (e.X > 420 && e.X < 485 && e.Y > 140 && e.Y < 150)
            {
                timerGameLoop.Stop();
            }
            else
            {
                if(_mole.Hit(e.X, e.Y))
                {
                    splat = true;
                    _splat.Left = _mole.Left - Resources.Splat.Width / 3;
                    _splat.Top = _mole.Top - Resources.Splat.Height / 3;

                    _hits++;
                }
                else
                {
                    _misses++;
                }
                _totalShots = _hits + _misses;
                _averageHits = (double)_hits / (double)_totalShots * 100.0;

            }
            FireGun();
        }

        private void FireGun()
        {
            /*
            SoundPlayer simpleSound = new SoundPlayer(Resources.Shotgun);

            simpleSound.Play();
            */
        }
    }
}
