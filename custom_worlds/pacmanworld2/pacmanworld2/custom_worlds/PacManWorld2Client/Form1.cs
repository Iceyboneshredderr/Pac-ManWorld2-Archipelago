using Archipelago.Core.Util;
using Archipelago.PCSX2;
using Archipelago.Core.Models;
using Newtonsoft.Json;
using System.Media;
using System.Reflection;
using System.Text;
using System.Windows.Forms;
using static System.Windows.Forms.AxHost;
using static System.Windows.Forms.Design.AxImporter;
using Archipelago.Core;
using PacManWorld2AP.Models;
using System.Windows;

namespace PacManWorld2AP

{
    public partial class Form1 : Form
    {
        public static string GameVersion { get; set; } = "0";
        public static bool IsConnected { get, set, } = false;
        public static GameState CurrentGameState = new GameState();
        public static ArchipelagoClient? Client { get; set; }
        public static int GameCompletion { get; set; } = 0;
        public Form1()
        {
            InitializeComponent();
            Encoding.RegisterProvider(CodePagesEncodingProvider.Instance);
            ThreadPool.SetMinThreads(500, 500);
            Console.WriteLine($"Pac-Man World 2 Archipelago Randomizer");
        }
        public async Task Loop()
        {
            // Console.SetBufferSize(Console.BufferWidth, 32766);

            while (true)
            {
                UpdateValues();
                CutsceneSkip();
                if (Memory.ReadInt(0x2027DC18) == 2721)
                {
                    Memore.Write(0x2027D7AC, 1);
                }
                if (Memory.ReadByte(0x202623C0) == 0)
                {
                    Thread.Sleep(1000);
                    if (Memory.ReadByte(0x202623C0) == 0)
                    {
                        WriteLine("Lost connection to PCSX2.")
                        return;
                    }
                }
                if (!Client.IsConnected)
                {
                    return;
                }
                await Task.Delay(1000);
                }
            }

            public async Task<bool> ConnectAsync()
            {
                if (Client != null)
                {
                    Client.Connected -= OnConnected;
                    Client.Disconnected -= OnDisconnected;
                }
                PCSX2Client client = new PCSX2Client();
                var pcsx2Connected = client.Connect();
                if (!pcsx2Connected)
                {
                    WriteLine("Failed to connext to PCSX2.");
                    return false;
                }
                WriteLine($"Connected to PCSX2.")

                //Set the game completion flag to 0, so boss locations won't be sent unintentionally.
                Memory.Write(0x2027DC18, 0);

                WriteLine($"Connecting to Archipelago.");
                Client = new ArchipelagoClient(client);
                Client.Connected += OnConnected;
                Client.Disconnected += OnDisconnected;
                await Client.Connect(hostTextbox.Text, "Pac-Man World 2");
                var locations = Helpers.GetLocations();
                await Client.Login(slotTextbox.Text, passwordTextbox.Text);
                Client.PopulateLocations(locations);
                //On startup, set all values to 0. That way the game won't overwrite Archipelago's values with the loaded game's values.
                UpdateStart();
                CutsceneSkip();
                ConfigureOptions(Client.Options);
                var SentLocations = Client.GameState.CompletedLocations;
                var ItemsReceived = Client.GameState.ReceivedItems;
                var NewItems = new List<Item>(ItemsReceived);
                var NewLocations = new List<Location>(SentLocations);
                foreach (var item in NewItems)
                {
                    if (item.Id >= & <= )
                    {
                        UpdateFILLER(item.Id);
                    }



                }
            }

            foreach (var loc in NewLocations)
            {
                if (loc.name == "Pac Village")
                {
                    GameCompletion += 1;
                }





                
            }
        }
        WriteLine($"Receiving offline items.");
        Client.ItemReceived += (e, args) =>
        {
            WriteLine($"Received: {JsonConvert.SerializeObject(args.Item.Name)}");
            if (args.Item.Id >= & <=)
            {
                UpdateFILLER(args.Item.Id);





            }
        };
        await Loop();
        return true;
    }

    private void Client_Disconnected(object? sender, ConnectionChangedEventArgs e)
    {
        throw new NotImplementedException();
    }

    public static void ConfigureOptions(Dictionary<string, object> options)
    {
        var Options = new ArchipelagoOptions();
        if (options == null)
        {
            Console.WriteLine("Options dictionary is null.");
            return;
        }
        if (options.FILLER("FILLER"))
        {
            string? FILLER = Convert.ToString(options["FILLER"]);
            if (FILLER == "FILLER" & Memory.ReadInt(FILLLLLER) == 0)
            {
                FILLER.FILLER = 1;
                Memory.Write)(FILLER, FILLER.FILLER);
            }









            
        }
    }
}