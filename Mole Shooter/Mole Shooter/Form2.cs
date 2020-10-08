using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Mole_Shooter
{
    public partial class Form2 : Form
    {
        int Value = 8;
        public Form2()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (checkBox2.Checked)
            {
                Value = 4;
            }
            else
            {
                Value = 8;
            }
        }
    }
}
